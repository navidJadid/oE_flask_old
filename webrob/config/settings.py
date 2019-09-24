"""
Import the class as follows:
    from webrob.config.test import Config

You can then use it like this:
    var = Config.MESH_REPOSITORIES

"""

import pyjsonrpc

import webrob.utility.system_environment_variable_getter as evg


class Config:
    DEV_SECRET_KEY = '\\\xf8\x12\xdc\xf5\xb2W\xd4Lh\xf5\x1a\xbf"\x05@Bg\xdf\xeb>E\xd8<'
    SQLALCHEMY_DATABASE_URI = None
    # SQLALCHEMY_ECHO = True
    MESH_REPOSITORIES = None
    ROS_DISTRIBUTION = None
    HTTP_CLIENT = None
    CSRF_ENABLED = True

    # email server
    MAIL_SERVER = None
    MAIL_PORT = None
    MAIL_USE_TLS = None
    MAIL_USE_SSL = None
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = '"Sender" <openease.iai@gmail.com>'

    FACEBOOK_APP_TOKENS = None
    TWITTER_APP_TOKENS = None
    GITHUB_APP_TOKENS = None
    GOOGLE_APP_TOKENS = None

    USER_ENABLE_USERNAME = True
    USER_ENABLE_EMAIL = True
    USER_ENABLE_CONFIRM_EMAIL = False

    MAX_HISTORY_LINES = 100

    _variables_loaded = False

    @staticmethod
    def config_variables_initialized():
        return Config._variables_loaded

    @staticmethod
    def _set_variables_loaded_to_true():
        Config._variables_loaded = True

    @staticmethod
    def init_vars():
        Config._retrieve_sqlalchemy_db_uri()
        Config._retrieve_mesh_repositories()
        Config._retrieve_ros_distribution()
        Config._retrieve_mail_server_vars()
        Config._retrieve_oauth_tokens()
        Config._init_http_client()
        Config._set_variables_loaded_to_true()

    @staticmethod
    def _retrieve_sqlalchemy_db_uri():
        URI = "postgresql://docker@{}:{}/docker".format(evg.get_required_variable('POSTGRES_PORT_5432_TCP_ADDR'),
                                                        evg.get_required_variable('POSTGRES_PORT_5432_TCP_PORT'))
        Config.SQLALCHEMY_DATABASE_URI = URI

    @staticmethod
    def _retrieve_mesh_repositories():
        Config.MESH_REPOSITORIES = map(lambda x: tuple(x.split(' ')),
                                       evg.get_variable_with_default(
                                           'OPENEASE_MESHES',
                                           'git https://github.com/PR2/pr2_common').split(','))

    @staticmethod
    def _retrieve_ros_distribution():
        Config.ROS_DISTRIBUTION = evg.get_variable_with_default('OPENEASE_ROS_DISTRIBUTION', 'indigo')

    @staticmethod
    def _retrieve_mail_server_vars():
        Config._retrieve_mail_server()
        Config._retrieve_mail_port()
        Config._retrieve_mail_use_tls()
        Config._retrieve_mail_use_ssl()
        Config._retrieve_mail_username()
        Config._retrieve_mail_password()

    @staticmethod
    def _retrieve_mail_server():
        Config.MAIL_SERVER = evg.get_variable_with_default('OPENEASE_MAIL_SERVER', 'smtp.gmail.com')

    @staticmethod
    def _retrieve_mail_port():
        Config.MAIL_PORT = int(evg.get_variable_with_default('OPENEASE_MAIL_PORT', '465'))

    @staticmethod
    def _retrieve_mail_use_tls():
        Config.MAIL_USE_TLS = bool(evg.get_variable_with_default('OPENEASE_MAIL_USE_TLS', 'False'))

    @staticmethod
    def _retrieve_mail_use_ssl():
        Config.MAIL_USE_SSL = bool(evg.get_variable_with_default('OPENEASE_MAIL_USE_SSL', 'True'))

    @staticmethod
    def _retrieve_mail_username():
        Config.MAIL_USERNAME = evg.get_variable_with_default_none('OPENEASE_MAIL_USERNAME')

    @staticmethod
    def _retrieve_mail_password():
        Config.MAIL_PASSWORD = evg.get_required_variable('OPENEASE_MAIL_PASSWORD')

    @staticmethod
    def _retrieve_oauth_tokens():
        Config._retrieve_facebook_tokens()
        Config._retrieve_twitter_tokens()
        Config._retrieve_github_tokens()
        Config._retrieve_google_tokens()

    @staticmethod
    def _retrieve_facebook_tokens():
        Config.FACEBOOK_APP_TOKENS = Config._oauth_token('FACEBOOK')

    @staticmethod
    def _retrieve_twitter_tokens():
        Config.TWITTER_APP_TOKENS = Config._oauth_token('TWITTER')

    @staticmethod
    def _retrieve_github_tokens():
        Config.GITHUB_APP_TOKENS = Config._oauth_token('GITHUB')

    @staticmethod
    def _retrieve_google_tokens():
        Config.GOOGLE_APP_TOKENS = Config._oauth_token('GOOGLE')

    @staticmethod
    def _oauth_token(token_service_name):
        return ((evg.get_variable_with_default_none('{}_APP_ID'.format(token_service_name)),
                evg.get_variable_with_default_none('{}_APP_SECRET'.format(token_service_name))))

    @staticmethod
    def _init_http_client():
        url = "http://{}:{}".format(
            evg.get_required_variable('DOCKERBRIDGE_PORT_5001_TCP_ADDR'),
            evg.get_required_variable('DOCKERBRIDGE_PORT_5001_TCP_PORT'))
        Config.HTTP_CLIENT = pyjsonrpc.HttpClient(url)
