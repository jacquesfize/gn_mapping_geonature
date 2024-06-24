"""add permissions

Revision ID: 9582541073
Revises: 4662728829
Create Date: 2024-06-24

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9582541073"
down_revision = "4662728829"  # A changer si modification faite dans le fichier [revisionID]_create_template_schema.py
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
            INSERT INTO gn_permissions.t_objects (code_object, description_object)
            VALUES (
                'MAPPING_GEONATURE', 
                'A module to map users/organisms which uses GeoNature'
            )
        """
    )
    op.execute(
        """
            INSERT INTO gn_permissions.cor_object_module
                (id_object, id_module)
            VALUES(
	            (SELECT id_object FROM gn_permissions.t_objects WHERE code_object = 'MAPPING_GEONATURE'),
	            (SELECT id_module FROM gn_commons.t_modules WHERE module_code = 'MAPPING_GEONATURE')
            )
        """
    )
    op.execute(
        """
        INSERT INTO
            gn_permissions.t_permissions_available (
                id_module,
                id_object,
                id_action,
                label,
                scope_filter
            )
        SELECT
            m.id_module,
            o.id_object,
            a.id_action,
            v.label,
            v.scope_filter
        FROM
            (
                VALUES
                    ('MAPPING_GEONATURE', 'MAPPING_GEONATURE', 'C', True, 'Créer des données'),
                    ('MAPPING_GEONATURE', 'MAPPING_GEONATURE', 'R', True, 'Voir des données'),
                    ('MAPPING_GEONATURE', 'MAPPING_GEONATURE', 'U', True, 'Modifier les données'),
                    ('MAPPING_GEONATURE', 'MAPPING_GEONATURE', 'V', True, 'Valider des données'),
                    ('MAPPING_GEONATURE', 'MAPPING_GEONATURE', 'E', True, 'Exporter des données'),
                    ('MAPPING_GEONATURE', 'MAPPING_GEONATURE', 'D', True, 'Supprimer des données')
            ) AS v (module_code, object_code, action_code, scope_filter, label)
        JOIN
            gn_commons.t_modules m ON m.module_code = v.module_code
        JOIN
            gn_permissions.t_objects o ON o.code_object = v.object_code
        JOIN
            gn_permissions.bib_actions a ON a.code_action = v.action_code
        """
    )
    op.execute(
        """
        WITH new_all_permissions AS (
            SELECT 
	            p.id_role,
	            p.id_action,
	            p.id_module,
	            (SELECT id_object FROM gn_permissions.t_objects WHERE code_object = 'MAPPING_GEONATURE') as id_object,
	            p.scope_value,
	            p.sensitivity_filter
            FROM 
	            gn_permissions.t_permissions p
            JOIN 
	            gn_commons.t_modules m
	            USING (id_module)
            JOIN
	            gn_permissions.t_objects o
	            USING (id_object)
            WHERE
	            m.module_code = 'MAPPING_GEONATURE'
	            AND o.code_object = 'ALL'
        )
        INSERT INTO gn_permissions.t_permissions
            (id_role, id_action, id_module, id_object, scope_value, sensitivity_filter)
        SELECT * FROM new_all_permissions
        """
    )
    op.execute(
        """
        WITH bad_permissions AS (
            SELECT
                p.id_permission
            FROM
                gn_permissions.t_permissions p
            JOIN gn_commons.t_modules m
                    USING (id_module)
            WHERE
                m.module_code = 'MAPPING_GEONATURE'
            EXCEPT
            SELECT
                p.id_permission
            FROM
                gn_permissions.t_permissions p
            JOIN gn_permissions.t_permissions_available pa ON
                (p.id_module = pa.id_module
                    AND p.id_object = pa.id_object
                    AND p.id_action = pa.id_action)
        )
        DELETE
        FROM
            gn_permissions.t_permissions p
                USING bad_permissions bp
        WHERE
            bp.id_permission = p.id_permission;
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM
            gn_permissions.t_permissions_available pa
        USING
            gn_commons.t_modules m
        WHERE
            pa.id_module = m.id_module
            AND
            module_code = 'MAPPING_GEONATURE'
        """
    )
    op.execute(
        """
        DELETE FROM
            gn_permissions.t_permissions p
        USING
            gn_commons.t_modules m,
            gn_permissions.t_objects o
        WHERE
            p.id_module = m.id_module
            AND
            module_code = 'MAPPING_GEONATURE'
            AND
            p.id_object = o.id_object
            AND
            code_object = 'MAPPING_GEONATURE'
        """
    )
    op.execute(
        "DELETE FROM gn_permissions.t_objects WHERE code_object = 'MAPPING_GEONATURE'"
    )
