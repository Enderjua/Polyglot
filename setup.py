#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

packages = set(open("requirements.txt", "r").read().splitlines())

requirements = filter(lambda x: "http" not in x, packages)


test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name="SyntaxMorph",
    version="1.0.0",
    author="Marijua",
    author_email="enderjua@gmail.com",
    description="SyntaxMorph is a Python module that enables code conversion between different programming languages",
    long_description=readme + '\n\n',
    url='https://github.com/Enderjua/SyntaxMorph',
    packages = ['morph'],
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='morph, syntax, python, syntaxmorph, ai, machinelearning, change, codexchange',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python',
    'Programming Language :: C++',
    'Programming Language :: Java',
    'Programming Language :: C',
    'Programming Language :: JavaScript',
    'Programming Language :: Ruby',
    'Programming Language :: PHP',
    'Programming Language :: Swift',
    'Programming Language :: Go',
    'Programming Language :: Kotlin',
    'Programming Language :: C#',
    'Programming Language :: TypeScript',
    'Programming Language :: Objective-C',
    'Programming Language :: Scala',
    'Programming Language :: Perl',
    'Programming Language :: Lua',
    'Programming Language :: Rust',
    'Programming Language :: R',
    'Programming Language :: Groovy',
    'Programming Language :: Dart',
    'Programming Language :: Haskell',
    'Programming Language :: Shell',
    'Programming Language :: Elixir',
    'Programming Language :: Clojure',
    'Programming Language :: Julia',
    'Programming Language :: F#',
    'Programming Language :: Visual Basic .NET',
    'Programming Language :: Erlang',
    'Programming Language :: Scheme',
    'Programming Language :: PL/SQL',
    'Programming Language :: COBOL',
    'Programming Language :: Fortran',
    'Programming Language :: Ada',
    'Programming Language :: ABAP',
    'Programming Language :: MATLAB',
    'Programming Language :: LabVIEW',
    'Programming Language :: Delphi',
    'Programming Language :: PowerShell',
    'Programming Language :: Lisp',
    'Programming Language :: Prolog',
    'Programming Language :: OCaml',
    'Programming Language :: Pascal',
    'Programming Language :: Apex',
    'Programming Language :: MQL4',
    'Programming Language :: MQL5',
    'Programming Language :: D',
    'Programming Language :: SAS',
    'Programming Language :: ALGOL',
    'Programming Language :: Smalltalk',
    'Programming Language :: AWK',
    'Programming Language :: Bash',
    'Programming Language :: Forth',
    'Programming Language :: Logo',
    'Programming Language :: Nim',
    'Programming Language :: Crystal',
    'Programming Language :: Elm',
    'Programming Language :: ActionScript',
    'Programming Language :: COBOLScript',
    'Programming Language :: VHDL',
    'Programming Language :: Tcl',
    'Programming Language :: Racket',
    'Programming Language :: PostScript',
    'Programming Language :: Haxe',
    'Programming Language :: Verilog',
    'Programming Language :: Simulink',
    'Programming Language :: Processing',
    'Programming Language :: AppleScript',
    'Programming Language :: XQuery',
    'Programming Language :: ColdFusion',
    'Programming Language :: QML',
    'Programming Language :: AMPL',
    'Programming Language :: Squirrel',
    'Programming Language :: Curl',
    'Programming Language :: Blockly',
    'Programming Language :: Ballerina',
    'Programming Language :: Idris',
    'Programming Language :: Reason',
    'Programming Language :: Scratch',
    'Programming Language :: Solidity',
    'Programming Language :: Stan',
    'Programming Language :: Red',
    'Programming Language :: Purescript',
    'Programming Language :: KRL',
    'Programming Language :: Unreal',
    'Programming Language :: Purescript',
    'Programming Language :: KRL',
    'Programming Language :: UnrealScript',
    'Programming Language :: JScript',
    'Programming Language :: AngelScript',
    'Programming Language :: Pike',
    'Programming Language :: Io',
    'Programming Language :: Magik',
    'Programming Language :: Rascal',
    'Programming Language :: Ring',
    'Programming Language :: Hack',
    'Programming Language :: AutoIt',
    'Programming Language :: Harbour',
    'Programming Language :: Nemerle',
    'Programming Language :: Opa',
    'Programming Language :: Vala',
    'Programming Language :: Vyper',
    'Programming Language :: Zig',
    'Programming Language :: Assembly',
    'Programming Language :: BASIC',
    'Programming Language :: VBA',
    'Programming Language :: SQL',
    'Programming Language :: MUMPS',
    'Programming Language :: PL/I',
    'Programming Language :: JCL',
    'Programming Language :: REXX',
    'Programming Language :: CMS-2',
    'Programming Language :: Jython',
    'Programming Language :: IronPython',
    'Programming Language :: RubyMotion',
    'Programming Language :: Kivy',
    'Programming Language :: Django',
    'Programming Language :: Flask',
    'Programming Language :: Pyramid',
    'Programming Language :: Rails',
    'Programming Language :: Sinatra',
    'Programming Language :: Hanami',
    'Programming Language :: Laravel',
    'Programming Language :: Symfony',
    'Programming Language :: CodeIgniter',
    'Programming Language :: Phalcon',
    'Programming Language :: Yii',
    'Programming Language :: FuelPHP',
    'Programming Language :: CakePHP',
    'Programming Language :: Slim',
    'Programming Language :: Zend Framework',
    'Programming Language :: Express',
    'Programming Language :: Meteor',
    'Programming Language :: Sails.js',
    'Programming Language :: Koa',
    'Programming Language :: Hapi',
    'Programming Language :: Spring',
    'Programming Language :: Play',
    'Programming Language :: Struts',
    'Programming Language :: Mojolicious',
    'Programming Language :: Catalyst',
    'Programming Language :: Phoenix',
    'Programming Language :: Ember',
    'Programming Language :: Angular',
    'Programming Language :: React',
    'Programming Language :: Vue.js',
    'Programming Language :: Backbone.js',
    'Programming Language :: Aurelia',
    'Programming Language :: Knockout',
    'Programming Language :: Mithril',
    'Programming Language :: Polymer',
    'Programming Language :: Dojo',
    'Programming Language :: Xamarin',
    'Programming Language :: Ionic',
    'Programming Language :: React Native',
    'Programming Language :: Flutter',
    'Programming Language :: NativeScript',
    'Programming Language :: PhoneGap',
    'Programming Language :: Cordova',
    'Programming Language :: Titanium',
    'Programming Language :: Qt',
    'Programming Language :: GTK',
    'Programming Language :: wxWidgets',
    'Programming Language :: Swing',
    'Programming Language :: JavaFX',
    'Programming Language :: Tkinter',
    'Programming Language :: PyQt',
    'Programming Language :: Kivy',
    'Programming Language :: Java AWT',
    'Programming Language :: SFML',
    'Programming Language :: SDL',
    'Programming Language :: Allegro',
    'Programming Language :: OpenGL',
    'Programming Language :: WebGL'
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Text Processing :: Linguistic',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
