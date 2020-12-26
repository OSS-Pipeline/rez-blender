name = "blender"

version = "2.90.1"

authors = [
    "Ton Roosendaal"
    "Blender Foundation"
]

description = \
    """
    Blender is a free and open-source 3D computer graphics software toolset used for creating animated films,
    visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality and
    computer games. Blender's features include 3D modeling, UV unwrapping, texturing, raster graphics editing,
    rigging and skinning, fluid and smoke simulation, particle simulation, soft body simulation, sculpting,
    animating, match moving, rendering, motion graphics, video editing, and compositing. 
    """

requires = [
    "cmake-3+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "blender"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "blender-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}")

    # Helper environment variables.
    env.BLENDER_BINARY_PATH.set("{root}")
