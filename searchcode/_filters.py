from typing import Literal, List


__all__ = ["CODE_LANGUAGES", "CODE_SOURCES", "get_language_ids", "get_source_ids"]

CODE_SOURCES = Literal[
    "Google Code",
    "GitHub",
    "BitBucket",
    "Sourceforge",
    "CodePlex",
    "Minix3",
    "Fedora Project",
    "Seek Quarry",
    "Tizen",
    "Gitorious",
    "Google Android",
    "GitLab",
    "Codeberg",
    "Repo.or.cz",
    "Sr.ht",
]

CODE_LANGUAGES = Literal[
    "XAML",
    "ASP.NET",
    "HTML",
    "Unknown",
    "MSBuild scripts",
    "C#",
    "XSD",
    "XML",
    "CMake",
    "C++ Header",
    "C++",
    "Makefile",
    "CSS",
    "Python",
    "MATLAB",
    "Objective C",
    "JavaScript",
    "Java",
    "PHP",
    "Erlang",
    "FORTRAN Legacy",
    "FORTRAN Modern",
    "C",
    "Lisp",
    "Visual Basic",
    "Shell",
    "Ruby",
    "Vim Script",
    "Assembly",
    "Objective C++",
    "Document Type Definition",
    "SQL",
    "YAML",
    "Ruby HTML",
    "Haskell",
    "Bash",
    "ActionScript",
    "MXML",
    "ASP",
    "D",
    "Pascal",
    "Scala",
    "Batch",
    "Groovy",
    "Extensible Stylesheet Language Transformations",
    "Perl",
    "Teamcenter def",
    "IDL",
    "Lua",
    "Go",
    "yacc",
    "Cython",
    "LEX",
    "Ada",
    "sed",
    "m4",
    "OCaml",
    "Smarty Template",
    "ColdFusion",
    "NAnt scripts",
    "Expect",
    "C Shell",
    "VHDL",
    "TCL",
    "JavaServer Pages",
    "SKILL",
    "AWK",
    "MUMPS",
    "SQL Data",
    "Korn Shell",
    "Patran Command Language",
    "DAL",
    "Fortran 95",
    "Octave",
    "Oracle Forms",
    "Dart",
    "COBOL",
    "Modula3",
    "Rexx",
    "Oracle Reports",
    "Softbridge Basic",
    "bc",
    "Teamcenter met",
    "Kermit",
    "Teamcenter mth",
    "AMPLE",
    "CCS",
    "JCL",
    "ABAP",
    "Clojure",
    "OpenCL",
    "CoffeeScript",
    "QML",
    "AutoHotkey",
    "ClojureScript",
    "ColdFusion CFScript",
    "gitignore",
    "Config",
    "Patch",
    "Markdown",
    "JSON",
    "Portable Object",
    "Certificate",
    "Hg Ignore",
    "MSBuild",
    "Windows Module Definition",
    "HLSL",
    "Sass",
    "LESS",
    "CUDA",
    "Swift",
    "Maven",
    "Visualforce Component",
    "Verilog-SystemVerilog",
    "JavaServer Faces",
    "Racket",
    "R",
    "Kotlin",
    "Powershell",
    "Rust",
    "Velocity Template Language",
    "Razor",
    "F#",
    "TypeScript",
    "NAnt script",
    "Ant",
    "Arduino Sketch",
    "Haml",
    "Grails",
    "Puppet",
    "Vala",
    "Windows Resource File",
    "Unity-Prefab",
    "Handlebars",
    "Robot Framework",
    "Pig Latin",
    "WiX source",
    "WiX include",
    "Mustache",
    "Windows Message File",
    "XQuery",
    "ECPP",
    "Visualforce Page",
    "WiX string localization",
    "Apex Trigger",
    "Vala Header",
    "xBase Header",
    "xBase",
    "InstallShield",
    "Harbour",
    "Forth",
    "PL/I",
    "CSON",
    "TeX",
    "Brainfuck",
    "Elixir",
    "zsh",
    "Julia",
    "dtrace",
    "Mathematica",
    "Standard ML",
    "SAS",
    "Haxe",
    "Nim",
    "TTCN",
    "Mercury",
    "Clean",
    "Prolog",
    "PureScript",
    "ERB",
    "Stylus",
    "XHTML",
    "Qt Project",
    "diff",
    "INI",
    "JSX",
    "Qt Linguist",
    "Qt",
    "Jam",
    "Protocol Buffers",
    "liquid",
    "Pug",
    "Freemarker Template",
    "XMI",
    "ClojureC",
    "Titanium Style Sheet",
    "Coq",
    "Crystal",
    "AspectJ",
    "EEx",
    "Elm",
    "Twig",
    "Slim",
    "Logtalk",
    "GDScript",
    "PowerBuilder",
    "Blade",
    "builder",
    "Visual Fox Pro",
    "SQL Stored Procedure",
    "License",
    "Agda",
    "Alchemist",
    "Alex",
    "Alloy",
    "Android Interface Definition Language",
    "Arvo",
    "AsciiDoc",
    "ATS",
    "Autoconf",
    "Basic",
    "Bazel",
    "Bitbake",
    "Bitbucket Pipeline",
    "Boo",
    "Bosque",
    "BuildStream",
    "C Header",
    "Cabal",
    "Cargo Lock",
    "Cassius",
    "Ceylon",
    "Closure Template",
    "Cogent",
    "Creole",
    "CSV",
    "Device Tree",
    "Dhall",
    "Docker ignore",
    "Dockerfile",
    "Emacs Dev Env",
    "Emacs Lisp",
    "F*",
    "FIDL",
    "Fish",
    "Flow9",
    "Fragment Shader File",
    "Futhark",
    "Game Maker Language",
    "Game Maker Project",
    "Gemfile",
    "Gherkin Specification",
    "GLSL",
    "GN",
    "Go Template",
    "Gradle",
    "Hamlet",
    "Happy",
    "HEX",
    "Idris",
    "ignore",
    "Intel HEX",
    "Isabelle",
    "Jade",
    "JAI",
    "Janet",
    "Jenkins Buildfile",
    "Jinja",
    "JSONL",
    "Julius",
    "Jupyter",
    "Just",
    "LaTeX",
    "LD Script",
    "Lean",
    "LOLCODE",
    "Lucius",
    "Luna",
    "Macromedia eXtensible Markup Language",
    "Madlang",
    "Mako",
    "Meson",
    "Module-Definition",
    "Monkey C",
    "MQL Header",
    "MQL4",
    "MQL5",
    "Nix",
    "nuspec",
    "Opalang",
    "Org",
    "Oz",
    "PKGBUILD",
    "PL/SQL",
    "Plain Text",
    "Polly",
    "Pony",
    "Processing",
    "Properties File",
    "PSL Assertion",
    "Q#",
    "QCL",
    "Rakefile",
    "Report Definition Language",
    "ReStructuredText",
    "Scheme",
    "Scons",
    "SPDX",
    "Specman e",
    "Spice Netlist",
    "SRecode Template",
    "Stata",
    "SVG",
    "Swig",
    "Systemd",
    "SystemVerilog",
    "TaskPaper",
    "Terraform",
    "Thrift",
    "TOML",
    "Twig Template",
    "TypeScript Typings",
    "Unreal Script",
    "Ur/Web",
    "Ur/Web Project",
    "V",
    "Varnish Configuration",
    "Verilog",
    "Verilog Args File",
    "Vertex Shader File",
    "Visual Basic for Applications",
    "Vue",
    "Web Services Description Language",
    "Wolfram",
    "Wren",
    "Xcode Config",
    "XML Schema",
    "Xtend",
    "Yarn",
    "Zig",
    "bait",
    "CloudFormation (JSON)",
    "CloudFormation (YAML)",
    "CodeQL",
    "DM",
    "Fennel",
    "FSL",
    "FXML",
    "hoon",
    "Nial",
    "ReasonML",
    "Sieve",
    "Solidity",
    "Teal",
    "TL",
]


def get_source_ids(source_names: List[CODE_SOURCES]) -> List[int]:
    """
    Gets a list of source IDs corresponding to the given source names.

    :param source_names: A list of source names to look up (e.g., "GitHub", "GitLab").
    :type source_names: List[CODE_SOURCES]
    :return: A list of IDs corresponding to the given source names.
    :rtype: List[int]
    """

    sources = {
        "Google Code": 1,
        "GitHub": 2,
        "BitBucket": 3,
        "Sourceforge": 4,
        "CodePlex": 5,
        "Minix3": 6,
        "Fedora Project": 7,
        "Seek Quarry": 8,
        "Tizen": 9,
        "Gitorious": 10,
        "Google Android": 12,
        "GitLab": 13,
        "Codeberg": 14,
        "Repo.or.cz": 15,
        "Sr.ht": 16,
    }

    return [sources[name] for name in source_names if name in sources]


def get_language_ids(language_names: List[CODE_LANGUAGES]) -> List:
    """
    Gets a list of language IDs corresponding to the given language names.

    :param language_names: A list of language names to look up (e.g., "Python", "JavaScript").
    :type language_names: List[CODE_LANGUAGES]
    :return: A list of IDs corresponding to the given language names.
    :rtype: List[int]
    """

    languages = {
        "XAML": 1,
        "ASP.NET": 2,
        "HTML": 3,
        "Unknown": 4,
        "MSBuild scripts": 5,
        "C#": 6,
        "XSD": 7,
        "XML": 8,
        "CMake": 14,
        "C++ Header": 15,
        "C++": 16,
        "Makefile": 17,
        "CSS": 18,
        "Python": 19,
        "MATLAB": 20,
        "Objective C": 21,
        "JavaScript": 22,
        "Java": 23,
        "PHP": 24,
        "Erlang": 25,
        "FORTRAN Legacy": 26,
        "FORTRAN Modern": 27,
        "C": 28,
        "Lisp": 29,
        "Visual Basic": 30,
        "Shell": 31,
        "Ruby": 32,
        "Vim Script": 33,
        "Assembly": 34,
        "Objective C++": 35,
        "Document Type Definition": 36,
        "SQL": 37,
        "YAML": 38,
        "Ruby HTML": 39,
        "Haskell": 40,
        "Bash": 41,
        "ActionScript": 42,
        "MXML": 43,
        "ASP": 44,
        "D": 45,
        "Pascal": 46,
        "Scala": 47,
        "Batch": 48,
        "Groovy": 49,
        "Extensible Stylesheet Language Transformations": 50,
        "Perl": 51,
        "Teamcenter def": 52,
        "IDL": 53,
        "Lua": 54,
        "Go": 55,
        "yacc": 56,
        "Cython": 57,
        "LEX": 59,
        "Ada": 61,
        "sed": 62,
        "m4": 63,
        "OCaml": 64,
        "Smarty Template": 65,
        "ColdFusion": 66,
        "NAnt scripts": 67,
        "Expect": 68,
        "C Shell": 69,
        "VHDL": 70,
        "TCL": 71,
        "JavaServer Pages": 72,
        "SKILL": 73,
        "AWK": 74,
        "MUMPS": 75,
        "SQL Data": 76,
        "Korn Shell": 78,
        "Patran Command Language": 83,
        "DAL": 84,
        "Fortran 95": 85,
        "Octave": 86,
        "Oracle Forms": 87,
        "Dart": 88,
        "COBOL": 89,
        "Modula3": 90,
        "Rexx": 91,
        "Oracle Reports": 92,
        "Softbridge Basic": 93,
        "bc": 94,
        "Teamcenter met": 95,
        "Kermit": 98,
        "Teamcenter mth": 99,
        "AMPLE": 100,
        "CCS": 101,
        "JCL": 102,
        "ABAP": 103,
        "Clojure": 104,
        "OpenCL": 105,
        "CoffeeScript": 106,
        "QML": 107,
        "AutoHotkey": 108,
        "ClojureScript": 109,
        "ColdFusion CFScript": 110,
        "gitignore": 111,
        "Config": 113,
        "Patch": 114,
        "Markdown": 118,
        "JSON": 122,
        "Portable Object": 126,
        "Certificate": 128,
        "Hg Ignore": 129,
        "MSBuild": 130,
        "Windows Module Definition": 131,
        "HLSL": 132,
        "Sass": 133,
        "LESS": 135,
        "CUDA": 136,
        "Swift": 137,
        "Maven": 139,
        "Visualforce Component": 140,
        "Verilog-SystemVerilog": 141,
        "JavaServer Faces": 142,
        "Racket": 143,
        "R": 144,
        "Kotlin": 145,
        "Powershell": 146,
        "Rust": 147,
        "Velocity Template Language": 148,
        "Razor": 149,
        "F#": 150,
        "TypeScript": 151,
        "NAnt script": 152,
        "Ant": 153,
        "Arduino Sketch": 154,
        "Haml": 155,
        "Grails": 156,
        "Puppet": 158,
        "Vala": 159,
        "Windows Resource File": 160,
        "Unity-Prefab": 161,
        "Handlebars": 162,
        "Robot Framework": 163,
        "Pig Latin": 164,
        "WiX source": 165,
        "WiX include": 166,
        "Mustache": 167,
        "Windows Message File": 168,
        "XQuery": 169,
        "ECPP": 172,
        "Visualforce Page": 173,
        "WiX string localization": 174,
        "Apex Trigger": 175,
        "Vala Header": 176,
        "xBase Header": 177,
        "xBase": 178,
        "InstallShield": 179,
        "Harbour": 180,
        "Forth": 181,
        "PL/I": 182,
        "CSON": 183,
        "TeX": 184,
        "Brainfuck": 185,
        "Elixir": 186,
        "zsh": 187,
        "Julia": 188,
        "dtrace": 189,
        "Mathematica": 190,
        "Standard ML": 191,
        "SAS": 192,
        "Haxe": 193,
        "Nim": 194,
        "TTCN": 195,
        "Mercury": 196,
        "Clean": 197,
        "Prolog": 198,
        "PureScript": 199,
        "ERB": 200,
        "Stylus": 201,
        "XHTML": 202,
        "Qt Project": 203,
        "diff": 204,
        "INI": 205,
        "JSX": 206,
        "Qt Linguist": 207,
        "Qt": 208,
        "Jam": 209,
        "Protocol Buffers": 210,
        "liquid": 211,
        "Pug": 212,
        "Freemarker Template": 213,
        "XMI": 214,
        "ClojureC": 215,
        "Titanium Style Sheet": 216,
        "Coq": 217,
        "Crystal": 218,
        "AspectJ": 220,
        "EEx": 221,
        "Elm": 222,
        "Twig": 223,
        "Slim": 224,
        "Logtalk": 225,
        "GDScript": 226,
        "PowerBuilder": 227,
        "Blade": 228,
        "builder": 229,
        "Visual Fox Pro": 230,
        "SQL Stored Procedure": 231,
        "License": 232,
        "Agda": 233,
        "Alchemist": 234,
        "Alex": 235,
        "Alloy": 236,
        "Android Interface Definition Language": 237,
        "Arvo": 238,
        "AsciiDoc": 239,
        "ATS": 240,
        "Autoconf": 241,
        "Basic": 242,
        "Bazel": 243,
        "Bitbake": 244,
        "Bitbucket Pipeline": 245,
        "Boo": 246,
        "Bosque": 247,
        "BuildStream": 248,
        "C Header": 249,
        "Cabal": 250,
        "Cargo Lock": 251,
        "Cassius": 252,
        "Ceylon": 253,
        "Closure Template": 254,
        "Cogent": 255,
        "Creole": 256,
        "CSV": 257,
        "Device Tree": 258,
        "Dhall": 259,
        "Docker ignore": 260,
        "Dockerfile": 261,
        "Emacs Dev Env": 262,
        "Emacs Lisp": 263,
        "F*": 265,
        "FIDL": 266,
        "Fish": 267,
        "Flow9": 268,
        "Fragment Shader File": 269,
        "Futhark": 270,
        "Game Maker Language": 271,
        "Game Maker Project": 272,
        "Gemfile": 273,
        "Gherkin Specification": 274,
        "GLSL": 275,
        "GN": 276,
        "Go Template": 277,
        "Gradle": 278,
        "Hamlet": 279,
        "Happy": 280,
        "HEX": 281,
        "Idris": 282,
        "ignore": 283,
        "Intel HEX": 284,
        "Isabelle": 285,
        "Jade": 286,
        "JAI": 287,
        "Janet": 288,
        "Jenkins Buildfile": 289,
        "Jinja": 290,
        "JSONL": 291,
        "Julius": 292,
        "Jupyter": 293,
        "Just": 294,
        "LaTeX": 295,
        "LD Script": 296,
        "Lean": 297,
        "LOLCODE": 298,
        "Lucius": 299,
        "Luna": 300,
        "Macromedia eXtensible Markup Language": 301,
        "Madlang": 302,
        "Mako": 303,
        "Meson": 304,
        "Module-Definition": 305,
        "Monkey C": 306,
        "MQL Header": 307,
        "MQL4": 308,
        "MQL5": 309,
        "Nix": 310,
        "nuspec": 311,
        "Opalang": 312,
        "Org": 313,
        "Oz": 314,
        "PKGBUILD": 315,
        "PL/SQL": 316,
        "Plain Text": 317,
        "Polly": 318,
        "Pony": 319,
        "Processing": 320,
        "Properties File": 321,
        "PSL Assertion": 322,
        "Q#": 323,
        "QCL": 324,
        "Rakefile": 325,
        "Report Definition Language": 326,
        "ReStructuredText": 327,
        "Scheme": 328,
        "Scons": 329,
        "SPDX": 330,
        "Specman e": 331,
        "Spice Netlist": 332,
        "SRecode Template": 333,
        "Stata": 334,
        "SVG": 335,
        "Swig": 336,
        "Systemd": 337,
        "SystemVerilog": 338,
        "TaskPaper": 339,
        "Terraform": 341,
        "Thrift": 342,
        "TOML": 343,
        "Twig Template": 344,
        "TypeScript Typings": 345,
        "Unreal Script": 346,
        "Ur/Web": 347,
        "Ur/Web Project": 348,
        "V": 349,
        "Varnish Configuration": 350,
        "Verilog": 351,
        "Verilog Args File": 352,
        "Vertex Shader File": 353,
        "Visual Basic for Applications": 354,
        "Vue": 355,
        "Web Services Description Language": 356,
        "Wolfram": 357,
        "Wren": 358,
        "Xcode Config": 359,
        "XML Schema": 360,
        "Xtend": 361,
        "Yarn": 362,
        "Zig": 363,
        "bait": 364,
        "CloudFormation (JSON)": 365,
        "CloudFormation (YAML)": 366,
        "CodeQL": 367,
        "DM": 368,
        "Fennel": 369,
        "FSL": 370,
        "FXML": 371,
        "hoon": 372,
        "Nial": 373,
        "ReasonML": 374,
        "Sieve": 375,
        "Solidity": 376,
        "Teal": 377,
        "TL": 378,
    }

    return [languages[name] for name in language_names if name in languages]
