# Sofia
> The funny, fully voiced *home assistant*

![Code Size](https://img.shields.io/github/languages/code-size/markovejnovic/Sofia?style=flat-square)
![Language](https://img.shields.io/github/languages/top/markovejnovic/Sofia?style=flat-square)
![Issues](https://img.shields.io/github/issues/markovejnovic/Sofia?style=flat-square)
![License](https://img.shields.io/github/license/markovejnovic/Sofia?style=flat-square)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)
- [Thank you](#thank-you)

## Features

> [Skyrim's most endorsed
> follower](https://www.google.com/search?client=firefox-b-d&q=sofia+follower)
> is back for more in **your home**.  The infamous Sofia needs little
> introduction as she causes trouble across your home. Experience a smart home
> in a whole new way with professional quality voice acting by the talented
> Christine Slagman (finalCrystine). -
> [Sofia](https://www.nexusmods.com/skyrim/mods/54527)

## Requirements

Sofia has a lot of dependencies.

First, get these with your favorite OS package manager (or compile them, I
shouldn't tell you how to live your life):
- `python2`
- `pip2`
- `virtualenv2`


## Installation

### Cloning

First clone the repository:
```bash
git clone https://github.com/markovejnovic/Sofia.git && cd Sofia
```

### Virtualenv

After fetching `python2`, `pip2` and `virtualenv2`, I'd advise you to create a
virtual environment in which Sofia's dependencies will be installed:
```bash
virtualenv venv
. venv/bin/activate # Only for bash (Probably this one if you're not sure)
. venv/bin/activate.fish # For Fish
```

### Dependencies

You can fetch most of the dependencies on *PyPI*, just run:
```bash
pip install cython numpy
pip install -r requirements.txt
```

### Snowboy

Installing [Snowboy](https://github.com/Kitt-AI/snowboy) is a fair bit more
demanding. I would recommend downloading the appropriate pre-compiled binaries
and their wrappers from [here](http://docs.kitt.ai/snowboy/#downloads). Please
also check the dependencies for _snowboy_ given
[here](https://snowboy.kitt.ai/docspartials/docs/index.html#quick-start). For a
_Rock64_, the installation is:
```bash
wget https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/pine64-debian-jessie-1.1.1.tar.bz2
mkdir snowboy
tar -xvjf pine64-debian-jessie-1.1.1.tar.bz2 -C snowboy --strip-components=1
rm pine64-debian-jessie-1.1.1.tar.bz2
```

### GPIO

Depending on your Pi-like device, you might have to edit the `import R64.GPIO
as GPIO` line in Sofia's files. Since I was using a [Rock
64](https://www.pine64.org/devices/single-board-computers/rock64/), this is
what I used. If, like me, you are using a *Rock 64*, you also need to execute 
the following in your Sofia directory to actually get the
[`R64`](https://github.com/Leapo/Rock64-R64.GPIO) library:
```bash
git clone https://github.com/Leapo/Rock64-R64.GPIO.git
mv Rock64-R64.GPIO/R64 .
rm -fr Rock64-R64.GPIO
```

For [Raspberry Pi](https://www.raspberrypi.org/), that line should look
something like `import RPi.GPIO as GPIO`. You can install the library with:
```bash
pip install RPi.GPIO
```
## Contributing

Hey, there's a lot of issues that need to be fixed! I'd really appreciate some
help. Make a pull request!

## FAQ

- _Does she work well?_
  - From my experience she will pick up about 75% of the time.
- _Why?_
  - I was thinking about a voice assistant while I was playing _Skyrim_.
  - Why not?

## Support
You can reach out to me here:
- [Website](https://markovejnovic.com/)
- [Instagram](marko.vejnovic.42)
- [LinkedIn](https://www.linkedin.com/in/markovejnovic/)

## License
This software is licensed under the GPLv3 license.

## Thank you
- A **BIG** thank you to
  [djjohnjarvis](https://www.nexusmods.com/skyrimspecialedition/users/3679820)
  for allowing the use of _Sofia_'s voicefiles.
- Thank you [fvcproductions](https://github.com/fvcproductions/) for your
  [README.md](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
  guide.
