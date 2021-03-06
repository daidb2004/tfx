# Lint as: python2, python3
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""Package dependencies for TFX."""


def make_required_install_packages():
  # Make sure to sync the versions of common dependencies (absl-py, numpy,
  # six, and protobuf) with TF.
  # TODO(b/130767399): add flask once the frontend is exposed externally.
  return [
      'absl-py>=0.1.6,<0.9',
      # LINT.IfChange
      'apache-beam[gcp]>=2.20,<3',
      # LINT.ThenChange(examples/chicago_taxi_pipeline/setup/setup_beam.sh)
      # TODO(b/149399451): remove once avro has a healthy release.
      ('avro-python3>=1.8.1,!=1.9.2.*,<2.0.0; '
       'python_version=="3.5" and platform_system=="Darwin"'),
      'click>=7,<8',
      'docker>=4.1,<5',
      'google-api-python-client>=1.7.8,<2',
      'grpcio>=1.28.1,<2',
      'jinja2>=2.7.3,<3',
      'kubernetes>=10.0.1,<12',
      # LINT.IfChange
      'ml-metadata>=0.21.2,<0.22',
      # LINT.ThenChange(//tfx/workspace.bzl)
      'protobuf>=3.7,<4',
      'pyarrow>=0.16,<0.17',
      'pyyaml>=5,<6',
      'six>=1.10,<2',
      # TODO(b/156035765): enable TF2.2.
      'tensorflow>=1.15,<2.2',
      'tensorflow-data-validation>=0.21.4,<0.22',
      'tensorflow-model-analysis>=0.21.4,<0.22',
      'tensorflow-serving-api>=1.15,<3',
      'tensorflow-transform>=0.21.2,<0.22',
      'tfx-bsl>=0.21.3,<0.22',
  ]


def make_required_test_packages():
  """Prepare extra packages needed for running unit tests."""
  # Note: It is okay to pin packages to exact verions in this list to minimize
  # conflicts.
  return [
      'apache-airflow>=1.10.10,<2',
      'kfp>=0.4,<0.5',
      'pytest>=5,<6',
  ]


def make_extra_packages_docker_image():
  # Packages needed for tfx docker image.
  return [
      'python-snappy>=0.5,<0.6',
  ]


def make_extra_packages_tfjs():
  # Packages needed for tfjs.
  return [
      'tensorflowjs>=1.7.3,<2',
  ]


def make_all_dependency_packages():
  # All extra dependencies.
  return make_required_test_packages() + make_extra_packages_tfjs()
