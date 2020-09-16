# Epigraph Conan package

This repo holds a [Conan](https://conan.io) recipe for the [Epigraph](https://github.com/EmbersArc/Epigraph) library.

The package is available on [Bintray](https://bintray.com/benjaminnavarro/bnavarro/epigraph%3Abnavarro).
To add the corresponding remote you can run:
```
conan remote add bnavarro https://api.bintray.com/conan/benjaminnavarro/bnavarro
```
And then use `epigraph/0.4.0@bnavarro/stable` as dependency in your conanfile.

Please note that there are no precompiled binaries currently available, so you have to use the `--build=missing` option when calling `conan install`, e.g: 
```
conan install . --build=missing
```