# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Installation

```bash
npm i
```

## Local Development

```bash
npm run start
# or
npm run start -- --locale ja
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Image Optimization

prepare ffmpeg

```bash
python md_img_convert.py --source ./docs --backup ./backup_images
```

## Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

```bash
npm run deploy
```

## Design Color

- Blue `#00C3BE`
- Green `#11f41d`
- Orange `#F48D11`