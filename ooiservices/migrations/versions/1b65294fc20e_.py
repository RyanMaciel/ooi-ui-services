"""empty message

Revision ID: 1b65294fc20e
Revises: 4ddc43e8e5b3
Create Date: 2015-01-12 10:28:12.311557

"""

# revision identifiers, used by Alembic.
revision = '1b65294fc20e'
down_revision = '4ddc43e8e5b3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arrays',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('array_code', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('geo_location', sa.Text(), nullable=True),
    sa.Column('array_name', sa.Text(), nullable=True),
    sa.Column('display_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('manufacturers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer_name', sa.Text(), nullable=False),
    sa.Column('phone_number', sa.Text(), nullable=True),
    sa.Column('contact_name', sa.Text(), nullable=True),
    sa.Column('web_address', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('assemblies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assembly_name', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('file_name', sa.Text(), nullable=False),
    sa.Column('file_system_path', sa.Text(), nullable=True),
    sa.Column('file_size', sa.Text(), nullable=True),
    sa.Column('file_permissions', sa.Text(), nullable=True),
    sa.Column('file_type', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('stream_parameters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_parameter_name', sa.Text(), nullable=True),
    sa.Column('short_name', sa.Text(), nullable=True),
    sa.Column('long_name', sa.Text(), nullable=True),
    sa.Column('standard_name', sa.Text(), nullable=True),
    sa.Column('units', sa.Text(), nullable=True),
    sa.Column('data_type', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('user_scopes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scope_name', sa.Text(), nullable=False),
    sa.Column('scope_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('deployments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('cruise_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('asset_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_type_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Text(), nullable=False),
    sa.Column('pass_hash', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('user_name', sa.Text(), nullable=True),
    sa.Column('active', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('confirmed_at', sa.Date(), nullable=True),
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('phone_primary', sa.Text(), nullable=True),
    sa.Column('phone_alternate', sa.Text(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], [u'ooiui_testing.organizations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_id'),
    schema='ooiui_testing'
    )
    op.create_table('assets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_type_id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('deployment_id', sa.Integer(), nullable=True),
    sa.Column('asset_name', sa.Text(), nullable=False),
    sa.Column('model', sa.Text(), nullable=True),
    sa.Column('current_lifecycle_state', sa.Text(), nullable=True),
    sa.Column('part_number', sa.Text(), nullable=True),
    sa.Column('firmware_version', sa.Text(), nullable=True),
    sa.Column('geo_location', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['asset_type_id'], [u'ooiui_testing.asset_types.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], [u'ooiui_testing.organizations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('instrument_models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instrument_model_name', sa.Text(), nullable=False),
    sa.Column('series_name', sa.Text(), nullable=True),
    sa.Column('class_name', sa.Text(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manufacturer_id'], [u'ooiui_testing.manufacturers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('user_scope_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('scope_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['scope_id'], [u'ooiui_testing.user_scopes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'ooiui_testing.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('instruments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instrument_name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('location_description', sa.Text(), nullable=True),
    sa.Column('instrument_series', sa.Text(), nullable=True),
    sa.Column('serial_number', sa.Text(), nullable=True),
    sa.Column('display_name', sa.Text(), nullable=True),
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('asset_id', sa.Integer(), nullable=False),
    sa.Column('depth_rating', sa.Float(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], [u'ooiui_testing.assets.id'], ),
    sa.ForeignKeyConstraint(['manufacturer_id'], [u'ooiui_testing.manufacturers.id'], ),
    sa.ForeignKeyConstraint(['model_id'], [u'ooiui_testing.instrument_models.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('inspection_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Text(), nullable=True),
    sa.Column('technician_name', sa.Text(), nullable=True),
    sa.Column('comments', sa.Text(), nullable=True),
    sa.Column('inspection_date', sa.Date(), nullable=True),
    sa.Column('document', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], [u'ooiui_testing.assets.id'], ),
    sa.ForeignKeyConstraint(['file_id'], [u'ooiui_testing.files.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('platforms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('platform_name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('location_description', sa.Text(), nullable=True),
    sa.Column('platform_series', sa.Text(), nullable=True),
    sa.Column('is_mobile', sa.Boolean(), nullable=False),
    sa.Column('serial_no', sa.Text(), nullable=True),
    sa.Column('asset_id', sa.Integer(), nullable=False),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], [u'ooiui_testing.assets.id'], ),
    sa.ForeignKeyConstraint(['manufacturer_id'], [u'ooiui_testing.manufacturers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('asset_file_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['asset_id'], [u'ooiui_testing.assets.id'], ),
    sa.ForeignKeyConstraint(['file_id'], [u'ooiui_testing.files.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('annotations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('modified_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('reference_name', sa.Text(), nullable=False),
    sa.Column('reference_type', sa.Text(), nullable=False),
    sa.Column('reference_pk_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'ooiui_testing.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('installation_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_id', sa.Integer(), nullable=False),
    sa.Column('assembly_id', sa.Integer(), nullable=False),
    sa.Column('date_installed', sa.Date(), nullable=True),
    sa.Column('date_removed', sa.Date(), nullable=True),
    sa.Column('technician_name', sa.Text(), nullable=True),
    sa.Column('comments', sa.Text(), nullable=True),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assembly_id'], [u'ooiui_testing.assemblies.id'], ),
    sa.ForeignKeyConstraint(['asset_id'], [u'ooiui_testing.assets.id'], ),
    sa.ForeignKeyConstraint(['file_id'], [u'ooiui_testing.files.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('drivers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instrument_id', sa.Integer(), nullable=True),
    sa.Column('driver_name', sa.Text(), nullable=False),
    sa.Column('driver_version', sa.Text(), nullable=True),
    sa.Column('author', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['instrument_id'], [u'ooiui_testing.instruments.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('streams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_name', sa.Text(), nullable=True),
    sa.Column('instrument_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['instrument_id'], [u'ooiui_testing.instruments.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('platform_deployments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('platform_id', sa.Integer(), nullable=True),
    sa.Column('reference_designator', sa.Text(), nullable=False),
    sa.Column('array_id', sa.Integer(), nullable=True),
    sa.Column('deployment_id', sa.Integer(), nullable=True),
    sa.Column('display_name', sa.Text(), nullable=True),
    sa.Column('geo_location', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['array_id'], [u'ooiui_testing.arrays.id'], ),
    sa.ForeignKeyConstraint(['deployment_id'], [u'ooiui_testing.deployments.id'], ),
    sa.ForeignKeyConstraint(['platform_id'], [u'ooiui_testing.platforms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('driver_stream_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('driver_id', sa.Integer(), nullable=False),
    sa.Column('stream_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['driver_id'], [u'ooiui_testing.drivers.id'], ),
    sa.ForeignKeyConstraint(['stream_id'], [u'ooiui_testing.streams.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('datasets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_id', sa.Integer(), nullable=False),
    sa.Column('deployment_id', sa.Integer(), nullable=False),
    sa.Column('process_level', sa.Text(), nullable=True),
    sa.Column('is_recovered', sa.Boolean(), server_default='false', nullable=False),
    sa.ForeignKeyConstraint(['deployment_id'], [u'ooiui_testing.deployments.id'], ),
    sa.ForeignKeyConstraint(['stream_id'], [u'ooiui_testing.streams.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('instrument_deployments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.Text(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('platform_deployment_id', sa.Integer(), nullable=True),
    sa.Column('instrument_id', sa.Integer(), nullable=True),
    sa.Column('reference_designator', sa.Text(), nullable=True),
    sa.Column('depth', sa.Float(), nullable=True),
    sa.Column('geo_location', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['instrument_id'], [u'ooiui_testing.instruments.id'], ),
    sa.ForeignKeyConstraint(['platform_deployment_id'], [u'ooiui_testing.platform_deployments.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('stream_parameter_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_id', sa.Integer(), nullable=False),
    sa.Column('parameter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parameter_id'], [u'ooiui_testing.stream_parameters.id'], ),
    sa.ForeignKeyConstraint(['stream_id'], [u'ooiui_testing.streams.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    op.create_table('dataset_keywords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('concept_name', sa.Text(), nullable=True),
    sa.Column('concept_description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], [u'ooiui_testing.datasets.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='ooiui_testing'
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dataset_keywords', schema='ooiui_testing')
    op.drop_table('stream_parameter_link', schema='ooiui_testing')
    op.drop_table('instrument_deployments', schema='ooiui_testing')
    op.drop_table('datasets', schema='ooiui_testing')
    op.drop_table('driver_stream_link', schema='ooiui_testing')
    op.drop_table('platform_deployments', schema='ooiui_testing')
    op.drop_table('streams', schema='ooiui_testing')
    op.drop_table('drivers', schema='ooiui_testing')
    op.drop_table('installation_records', schema='ooiui_testing')
    op.drop_table('annotations', schema='ooiui_testing')
    op.drop_table('asset_file_link', schema='ooiui_testing')
    op.drop_table('platforms', schema='ooiui_testing')
    op.drop_table('inspection_status', schema='ooiui_testing')
    op.drop_table('instruments', schema='ooiui_testing')
    op.drop_table('user_scope_link', schema='ooiui_testing')
    op.drop_table('instrument_models', schema='ooiui_testing')
    op.drop_table('assets', schema='ooiui_testing')
    op.drop_table('users', schema='ooiui_testing')
    op.drop_table('asset_types', schema='ooiui_testing')
    op.drop_table('deployments', schema='ooiui_testing')
    op.drop_table('user_scopes', schema='ooiui_testing')
    op.drop_table('organizations', schema='ooiui_testing')
    op.drop_table('stream_parameters', schema='ooiui_testing')
    op.drop_table('files', schema='ooiui_testing')
    op.drop_table('assemblies', schema='ooiui_testing')
    op.drop_table('manufacturers', schema='ooiui_testing')
    op.drop_table('arrays', schema='ooiui_testing')
    ### end Alembic commands ###
