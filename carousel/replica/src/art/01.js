/* 01 — Set realistic study targets.
 * Student writing at a desk: study-plan checklist pinned top right, a stack of
 * PLAN / FOCUS / ACHIEVE books and a dartboard on the desk's front corner. */
const { C, W, sh, fl, ln, circ, dot, rect, label, limbUnder, limbOver, coilyHair } = require('./_kit');

module.exports = function scene() {
  const tee = '#2A4668', teeShade = '#1D3450';
  const board = '#F7E6C2', boardEdge = '#D9B77A';

  /* --- ground shapes --------------------------------------------------- */
  const ground = `
    ${dot(925, 55, 46, C.goldBlob)}
    ${fl('M0 660 Q 96 646 132 724 Q 168 802 118 862 Q 78 930 122 1000 L 0 1000 Z', C.blueBlob)}`;

  /* --- study plan card ------------------------------------------------- */
  const rows = [1, 2, 3, 4].map((n, i) => {
    const y = 252 + i * 50;
    return `
      ${rect(783, y - 20, 33, 33, 'none', 3, W.detail)}
      ${ln(`M 789 ${y - 5} L 797 ${y + 5} L 811 ${y - 15}`, 3.4)}
      ${label(880, y + 6, `TOPIC ${n}`, 27, C.outline, 900, 'letter-spacing="0.6"')}
      ${ln(`M 783 ${y + 21} L 952 ${y + 21}`, 1.6, boardEdge)}`;
  }).join('');

  const plan = `
    <g transform="rotate(-1.2 857 295)">
      ${rect(744, 139, 226, 311, board, 7, W.detail)}
      ${label(857, 200, 'STUDY PLAN', 33, C.outline, 900, 'letter-spacing="1.2"')}
      ${ln('M 762 218 L 952 218', 2, boardEdge)}
      ${rows}
    </g>`;

  /* --- head and face --------------------------------------------------- */
  const head = `
    ${limbUnder('M 668 448 L 674 520', 58)}
    ${limbOver('M 668 448 L 674 520', 58, C.skinShade)}

    ${sh('M 600 350 Q 598 288 660 282 Q 736 280 748 342 Q 760 428 720 470 Q 688 498 654 486 Q 610 462 602 400 Z', C.skin)}
    ${fl('M 706 300 Q 748 320 748 372 Q 754 438 718 470 Q 738 410 730 352 Q 724 314 706 300 Z', C.skinLit)}
    ${sh('M 604 358 Q 578 352 578 380 Q 578 408 606 410', C.skin, W.detail)}
    ${ln('M 590 374 Q 598 380 596 392', 2)}

    ${coilyHair(680, 350, 98, 96, { bumps: 12, from: 204, to: -22, brow: 0.42 })}
    ${fl('M 618 296 Q 668 258 730 274 Q 690 268 654 288 Q 630 302 618 296 Z', C.hairLit)}

    ${ln('M 640 382 Q 660 372 680 380', 3.6)}
    ${ln('M 708 378 Q 726 370 742 380', 3.6)}
    ${fl('M 644 404 Q 664 394 684 406 Q 664 416 644 404 Z', C.outline)}
    ${fl('M 708 402 Q 726 392 742 404 Q 724 412 708 402 Z', C.outline)}
    ${ln('M 684 414 Q 680 444 694 458 Q 684 464 672 458', 3)}
    ${ln('M 662 476 Q 682 486 704 474', 3.2)}
    ${ln('M 610 424 Q 628 464 660 482', 2.2, C.skinShade)}`;

  /* --- torso ----------------------------------------------------------- */
  const torso = `
    ${sh('M 391 1000 Q 392 700 428 630 Q 470 546 604 522 L 726 520 Q 822 534 856 606 Q 890 676 892 1000 Z', tee)}
    ${fl('M 780 534 Q 856 574 872 662 Q 890 748 890 1000 L 826 1000 Q 828 726 806 648 Q 790 572 780 534 Z', teeShade)}
    ${ln('M 616 528 Q 650 574 700 570 Q 726 566 736 534', 2.8, teeShade)}`;

  /* --- desk, in front of the seated figure ----------------------------- */
  const desk = `
    ${sh('M 1002 632 L 588 668 Q 452 682 432 792 Q 414 900 520 918 L 1002 928 Z', C.woodLit)}
    ${fl('M 1002 906 L 520 926 Q 456 922 430 892 Q 452 942 528 948 L 1002 956 Z', C.woodDark)}
    ${ln('M 986 690 L 676 708', 2, C.woodDark)}
    ${ln('M 986 756 L 606 780', 2, C.woodDark)}
    ${ln('M 986 826 L 566 848', 2, C.woodDark)}`;

  /* --- mug and its plant, standing on the desk ------------------------- */
  const leaf = (cx, cy, rx, ry, a) =>
    `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${C.blueLit}" ` +
    `stroke="${C.blueDeep}" stroke-width="2" transform="rotate(${a} ${cx} ${cy})"/>`;

  const mug = `
    ${ln('M 942 626 L 942 548', 2.4, C.blueDeep)}
    ${leaf(912, 572, 28, 11, -38)}${leaf(972, 566, 27, 10, 34)}
    ${leaf(920, 606, 24, 9, -16)}${leaf(966, 602, 23, 9, 18)}
    ${leaf(938, 540, 10, 26, -6)}
    ${sh('M 903 626 L 982 626 L 975 706 Q 973 716 962 716 L 924 716 Q 913 716 911 706 Z', C.navyLine)}
    ${sh('M 982 644 Q 1004 650 1002 666 Q 1000 684 982 688', 'none', W.detail)}`;

  /* --- open book ------------------------------------------------------- */
  const rules = (x0, x1, y0, n, step, skew) =>
    Array.from({ length: n }, (_, i) =>
      ln(`M ${x0} ${y0 + i * step} L ${x1} ${y0 + i * step + skew}`, 2.2, '#C9BEA9')).join('');

  const book = `
    ${sh('M 742 694 Q 620 684 528 710 L 542 834 Q 638 808 744 820 Z', '#F5F0E3')}
    ${sh('M 742 694 Q 862 680 964 708 L 950 836 Q 848 806 744 820 Z', '#F5F0E3')}
    ${rules(556, 728, 728, 5, 20, 4)}
    ${rules(758, 938, 724, 5, 20, -3)}
    ${ln('M 742 696 L 744 820', 2.8)}
    ${fl('M 734 812 Q 744 826 754 812 Q 744 822 734 812 Z', C.outline)}`;

  /* --- arms, lying along the desk -------------------------------------- */
  const armL = 'M 424 590 Q 396 660 424 692 Q 468 716 546 700';
  const armR = 'M 836 566 Q 878 596 900 646';
  const arms = `
    ${limbUnder(armL, 58)}${limbUnder(armR, 58)}
    ${limbOver(armL, 58, C.skin)}${limbOver(armR, 58, C.skin)}
    ${fl('M 860 584 Q 894 610 912 654 L 878 672 Q 862 626 838 596 Z', C.skinShade)}

    ${sh('M 856 636 Q 902 630 926 654 Q 946 682 918 700 Q 872 714 842 694 Q 820 672 834 652 Z', C.skin)}
    ${ln('M 856 668 Q 886 662 910 672', 2.4, C.skinShade)}
    ${ln('M 854 688 Q 882 682 906 690', 2.4, C.skinShade)}

    ${sh('M 546 668 Q 588 646 634 660 Q 676 676 668 710 Q 656 748 606 750 Q 556 748 540 722 Q 530 692 546 668 Z', C.skin)}
    ${ln('M 574 674 Q 608 672 634 686', 2.4, C.skinShade)}
    ${ln('M 566 700 Q 604 696 638 710', 2.4, C.skinShade)}
    ${ln('M 570 724 Q 600 722 626 730', 2.4, C.skinShade)}
    ${ln('M 569 599 L 662 735', 10, C.navyLine)}
    ${fl('M 654 726 L 668 748 L 662 720 Z', C.outline)}`;

  /* --- book stack, drawn bottom-up so each sits on the one below -------- */
  const slab = (y, faceFill, topFill, text, shift) => `
    <g transform="translate(${shift} 0) rotate(-4.5 428 ${y})">
      ${sh(`M 300 ${y} L 552 ${y - 14} L 558 ${y + 36} Q 558 ${y + 46} 546 ${y + 47} L 310 ${y + 60} Q 298 ${y + 60} 298 ${y + 50} Z`, faceFill)}
      ${sh(`M 300 ${y} Q 318 ${y - 24} 342 ${y - 26} L 540 ${y - 38} Q 556 ${y - 36} 552 ${y - 14} Z`, topFill)}
      ${label(430, y + 36, text, 31, C.white, 900, 'letter-spacing="1.6"')}
    </g>`;

  const stack = `
    ${slab(858, '#C9743A', '#D9884C', 'ACHIEVE', 14)}
    ${slab(796, '#4B5B33', '#5B6C40', 'FOCUS', 6)}
    ${slab(734, '#3C5F7E', '#4E7391', 'PLAN', 0)}`;

  /* --- dartboard -------------------------------------------------------- */
  const ring = (r, sw) =>
    `<circle cx="198" cy="765" r="${r}" fill="none" stroke="#CB5931" stroke-width="${sw}"/>`;
  const target = `
    ${circ(198, 765, 90, C.cream, 0)}
    ${ring(84, 13)}${ring(56, 13)}
    ${dot(198, 765, 15, '#CB5931')}
    ${ln('M 292 676 L 206 758', 9, C.navy)}
    ${fl('M 302 666 L 266 674 L 294 702 Z', C.navy)}
    ${fl('M 280 688 L 254 694 L 274 714 Z', C.navy)}`;

  return ground + plan + head + torso + desk + mug + book + arms + stack + target;
};
