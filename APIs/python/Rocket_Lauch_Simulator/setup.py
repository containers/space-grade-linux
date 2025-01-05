# setup.py
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup, find_packages

setup(
    name='rocket_launcher',
    version='0.1.0',
    description='A rocket launch simulation package.',
    author='Douglas Schilling Landgraf, Leonardo Rossetti, Dan Walsh',
    author_email='dougsland@redhat.com, lrossett@redhat.com, dwalsh@redhat.com',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'rclpy',
        'std_msgs',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

