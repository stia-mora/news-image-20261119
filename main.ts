// news-image-20261119 entry point (Node 22, standard library only).
//
// The entry is the PNG file sitting next to this script. This program copies
// it, byte for byte, into the output directory the grader provides, so the
// judge sees exactly the image in this repository.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// MAKEFUN_OUTPUT_DIR defaults to /output when unset. The destination folder
// is created if it does not exist yet.

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });

const target = join(outDir, 'entry.png');
copyFileSync(source, target);
console.log(`entry.png -> ${target}`);
