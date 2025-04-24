<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/room-crawler/master/game/gui/window_icon.png" alt="Room Crawler">
</p>

# Room Crawler

![release](https://img.shields.io/github/v/release/remarkablegames/room-crawler)
[![build](https://github.com/remarkablegames/room-crawler/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/room-crawler/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/room-crawler/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/room-crawler/actions/workflows/lint.yml)

🚪 Room Crawler

Play the game on:

- [remarkablegames](https://remarkablegames.org/room-crawler)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

### Audio

- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/room-crawler.git
cd room-crawler
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to display the developer menu.

Clean the cache:

```sh
find game -name "*.rpyc" -delete
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
