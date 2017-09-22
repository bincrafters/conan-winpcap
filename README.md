[![Build status](https://ci.appveyor.com/api/projects/status/e91iaablbidrl5br?svg=true)](https://ci.appveyor.com/project/uilianries/conan-winpcap-y64ie) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![badge](https://img.shields.io/badge/conan.io-winpcap%2F4.1.3-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/winpcap/4.1.3/bincrafters/stable)
[![Download](https://api.bintray.com/packages/bincrafters/public-conan/winpcap%3Abincrafters/images/download.svg?version=4.1.3%3Astable)](https://bintray.com/bincrafters/oublic-conan/winpcap%3Abincrafters/4.1.3%3Astable/link)

## WinPCAP library is an API for capturing network traffic for Windows

![conan-winpcap](conan-winpcap.png)

[Conan.io](https://conan.io) package for [winpcap](https://github.com/wireshark/winpcap) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/conan/winpcap%3Abincrafters).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload winpcap/4.1.3@bincrafters/stable --all

## Reuse the packages

### Basic setup

    $ conan install winpcap/4.1.3@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    winpcap/4.1.3@bincrafters/stable

    [options]
    shared=True

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[BSD](LICENSE)
