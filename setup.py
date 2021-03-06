from setuptools import setup, find_packages
import sys
import versioneer

install_requires = ['menpo>=0.4.0,<0.5',
                    'cyassimp>=0.2,<0.3',
                    'cyrasterize>=0.2,<0.3']

# These dependencies currently don't work on Python 3
if sys.version_info.major == 2:
    install_requires.append('mayavi>=4.4,<4.5')
    install_requires.append('menpo-pyvrml97==2.3.0a4')

setup(name='menpo3d',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='MenpoKit providing tools for 3D Computer Vision research',
      author='James Booth',
      author_email='james.booth08@imperial.ac.uk',
      packages=find_packages(),
      package_data={'menpo3d': ['data/*']},
      install_requires=install_requires,
      tests_require=['nose', 'mock']
)
