import os
import xacro
import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share_path = get_package_share_directory('sample_diff_drive_sensor_kit_description')
    urdf_xacro_path = os.path.join(pkg_share_path, 'urdf/sensors.xacro')
    urdf_xacro = xacro.process_file(urdf_xacro_path)
    urdf_xml = urdf_xacro.toprettyxml()
    rsp = launch_ros.actions.Node(package='robot_state_publisher',
                                  executable='robot_state_publisher',
                                  output='screen',
                                  parameters=[
                                      {'robot_description': urdf_xml}
                                  ])
    jsp = launch_ros.actions.Node(package='joint_state_publisher_gui',
                                  executable='joint_state_publisher_gui',
                                  output='screen')
    rviz_cfg_dir = os.path.join(pkg_share_path, 'config/sensors_calibration.rviz')
    rviz = launch_ros.actions.Node(package='rviz2',
                                   executable='rviz2',
                                   output='screen',
                                   arguments=['-d', rviz_cfg_dir])
    return launch.LaunchDescription([rsp, jsp, rviz])
