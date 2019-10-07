# *********************Settings Test Constants**********************

MAIL_PASSWORD = 'abc'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'Paul'
FBOOK_APP_TOKENS = ('Paul01', 'abCD123ef')
TWIT_APP_TOKENS = ('Paul01', 'abCDef123hi')
GIT_APP_TOKENS = ('Paul01', 'abCD-ef123hi')
GOOGLE_APP_TOKENS = ('Paul01', 'abCD-ef123hi/456')
SERVICE_TOKENS = ('Paul01', 'abCD-ef123hi/456')
ROS_DISTRIBUTION = 'indigo'
SQLALCHEMY_DATABASE_URI = 'postgresql://docker@127.0.0.1:5432/docker'
POSTGRES_PORT_5432_TCP_ADDR = '127.0.0.1'
POSTGRES_PORT_5432_TCP_PORT = '5432'
NULL_TOKENS = (None,None)

DOCKBRIDGE_PORT_5001_TCP_ADDR = '170.17.0.60'
DOCKBRIDGE_PORT_5001_TCP_PORT = '5001'

URL = 'http://170.17.0.60:5001'

OAUTH_TOKENS = ('Paul01', 'abCD-ef123hi/456')

GIT_REPO = 'git https://github.com/PR2/pr2_common'
SVN_REPO = 'svn https://svn.com/PR2/pr2_common'
OPENEASE_MESHES = '{},{}'.format(GIT_REPO,SVN_REPO)
MESH_REPOSITORIES = [('git', 'https://github.com/PR2/pr2_common'), ('svn', 'https://svn.com/PR2/pr2_common')]
MESH_REPO_DEFAULT = [('git', 'https://github.com/PR2/pr2_common')]



