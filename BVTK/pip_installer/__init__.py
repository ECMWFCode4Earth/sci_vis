# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   pip_installer/__init__.py
#
#   Functions to automatically install pip packages on Blender's python.
# ---------------------------------------------------------------------------------


import socket
import importlib
import bpy
import subprocess
from .. utilities import *


def is_connected():
    remote_server = "www.google.com"
    try:
        host = socket.gethostbyname(remote_server)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


def pip_update():
    if not is_connected():
        return
    log.info("Updating pip.")
    try:
        get_pip = os.path.join(addon_path, "pip_installer/get-pip.py")
        log.info(subprocess.run([bpy.app.binary_path_python, get_pip], check=True,
                                stderr=subprocess.PIPE, stdout=subprocess.PIPE))
        log.info("Pip updated.")
        return True
    except subprocess.CalledProcessError as e:
        message = (
            "Pip update failed.\n"
            "Output:      {}\n"
            "Stdout:      {}\n"
            "Stderr:      {}\n".format(e.output, e.stdout, e.stderr)
        )
        log.debug(message)
        log.warning("Pip update failed. Updating pip is usually necessary, the following\n"
                    "attempts to install the required libraries may fail.")
    return False


def pip_install(package, dependencies=()):
    """Try to install the specified package using pip.
    Return codes are:
    -1: Failure (no internet)
    0:  Failure (command failed)
    1:  Success
    """
    pip_update()
    return __pip_install(package, dependencies)


def __pip_install(package, dependencies=()):
    try:
        importlib.import_module(package)
        return 1
    except ImportError:
        pass

    for dep in dependencies:
        __pip_install(dep)

    cmd = "python3 pip install {}".format(package)

    if not is_connected():
        log.error("Unable to connect to the internet. Connection is required\n"
                  "to install the '{}' package. Connect to the internet and try\n"
                  "again (just close and reopen blender), or install the\n"
                  "package yourself by running the command '{}'.".format(package, cmd))
        return -1

    log.info("Installing {} via pip.".format(package))

    args = [bpy.app.binary_path_python, "-m", "pip", "install"]
    if len(dependencies):
        # If dependencies are specified they will be installed separately
        # This is needed to avoid creating duplicates of libraries already
        # installed inside Blender (for example numpy)
        args.append("--no-dependencies")
    args.append(package)

    try:
        subprocess.run(args, check=True,
                       stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        message = (
            "Command '{}' failed.\n"
            "Output:      {}\n"
            "Stdout:      {}\n"
            "Stderr:      {}\n".format(args, e.output, e.stdout, e.stderr)
        )
        log.debug(message)

    try:
        importlib.import_module(package)
        log.info("{} package successfully installed.".format(package))
        return 1
    except ImportError:
        log.error("{} package failed to install. You can try to install it yourself by "
                  "running the command '{}'.".format(package, cmd))

    return 0


def is_loaded(package):
    if package in globals():
        return True
    try:
        import importlib
        importlib.import_module(package)
    except ImportError:
        return False
    return True
