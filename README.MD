####################
 EasyNuitka User Manual
####################

**********
 Overview
**********
EasyNuitka is a Nuitka-based packaging tool with a graphical interface


![alt tag](http://cad-upyun.test.upcdn.net/EasyNuitka/EasyNuitka.png)
*******
 Usage
*******

Requirements
============

-  C Compiler: You need a compiler with support for C11 or alternatively
   for C++03 [#]_

   Currently this means, you need to use one of these compilers:

   -  The MinGW64 C11 compiler on Windows, must be based on gcc 11.2 or
      higher. It will be *automatically* downloaded if no usable C
      compiler is found, which is the recommended way of installing it,
      as Nuitka will also upgrade it for you.

   -  Visual Studio 2022 or higher on Windows [#]_, older versions will
      work but only supported for commercial users. Configure to use the
      English language pack for best results (Nuitka filters away
      garbage outputs, but only for English language). It will be used
      by default if installed.

   -  On all other platforms, the ``gcc`` compiler of at least version
      5.1, and below that the ``g++`` compiler of at least version 4.4
      as an alternative.

   -  The ``clang`` compiler on macOS X and most FreeBSD architectures.

   -  On Windows the ``clang-cl`` compiler on Windows can be used if
      provided by the Visual Studio installer.

-  Python: Version 2.6, 2.7 or 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10

   .. important::

      For Python 3.3/3.4 and *only* those, we need other Python version
      as a *compile time* dependency.

      Nuitka itself is fully compatible with all listed versions, but
      Scons as an internally used tool is not.

      For these versions, you *need* a Python2 or Python 3.5 or higher
      installed as well, but only during the compile time only. That is
      for use with Scons (which orchestrates the C compilation), which
      does not support the same Python versions as Nuitka.

      In addition, on Windows, Python2 cannot be used because
      ``clcache`` does not work with it, there a Python 3.5 or higher
      needs to be installed.

      Nuitka finds these needed Python versions (e.g. on Windows via
      registry) and you shouldn't notice it as long as they are
      installed.

      Increasingly, other functionality is available when another Python
      has a certain package installed. For example, onefile compression
      will work for a Python 2.x when another Python is found that has
      the ``zstandard`` package installed.

   .. admonition:: Moving binaries to other machines

      The created binaries can be made executable independent of the
      Python installation, with ``--standalone`` and ``--onefile``
      options.

   .. admonition:: Binary filename suffix

      The created binaries have an ``.exe`` suffix on Windows. On other
      platforms they have no suffix for standalone mode, or ``.bin``
      suffix, that you are free to remove or change, or specify with the
      ``-o`` option.

      The suffix for acceleration mode is added just to be sure that the
      original script name and the binary name do not ever collide, so
      we can safely do an overwrite without destroying the original
      source file.

   .. admonition:: It **has to** be CPython, Anaconda Python.

      You need the standard Python implementation, called "CPython", to
      execute Nuitka, because it is closely tied to implementation
      details of it.

   .. admonition:: It **cannot be** from Windows app store

      It is known that Windows app store Python definitely does not
      work, it's checked against. And on macOS "pyenv" likely does
      **not** work.

-  Operating System: Linux, FreeBSD, NetBSD, macOS X, and Windows (32/64
   bits).

   Others may work as well. The portability is expected to be generally
   good, but the e.g. Scons usage may have to be adapted. Make sure to
   match Windows Python and C compiler architecture, or else you will
   get cryptic error messages.

-  Architectures: x86, x86_64 (amd64), and arm, likely many more

   Other architectures are expected to also work, out of the box, as
   Nuitka is generally not using any hardware specifics. These are just
   the ones tested and known to be good. Feedback is welcome. Generally,
   the architectures that Debian supports can be considered good and
   tested too.

.. [#]

   Support for this C11 is a given with gcc 5.x or higher or any clang
   version.

   The MSVC compiler doesn't do it yet. But as a workaround, as the C++03
   language standard is very overlapping with C11, it is then used instead
   where the C compiler is too old. Nuitka used to require a C++ compiler
   in the past, but it changed.

.. [#]

   Download for free from
   https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx
   (the community editions work just fine).

   The latest version is recommended but not required. On the other hand,
   there is no need to except pre-Windows 10 support, and they might work
   for you, but support of these configurations is only available to
   commercial users.


Installation
============

For most systems, there will be packages on the `download page
<https://nuitka.net/doc/download.html>`__ of Nuitka. But you can also
install it from source code as described above, but also like any other
Python program it can be installed via the normal ``python setup.py
install`` routine.

License
=======

Nuitka is licensed under the Apache License, Version 2.0; you may not
use it except in compliance with the License.

You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

*************************************
 Tutorial Setup and build on Windows
*************************************

This is basic steps if you have nothing installed, of course if you have
any of the parts, just skip it.

Setup
=====

Install Python
--------------

-  Download and install Python from
   https://www.python.org/downloads/windows

-  Select one of ``Windows x86-64 web-based installer`` (64 bits Python,
   recommended) or ``x86 executable`` (32 bits Python) installer.

-  Verify it's working using command ``python --version``.

Install Nuitka
--------------

-  ``python -m pip install nuitka``

-  Verify using command ``python -m nuitka --version``

Install EasyNuitka
--------------
- ``python -m pip install EasyNuitka``

RUN EasyNuitka
--------------
- ``python -m EasyNuitka``


Help
--------------
You will find the current version at:
https://nuitka.net/doc/user-manual.html