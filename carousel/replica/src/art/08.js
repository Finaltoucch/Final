/* 08 — We wish you all the best in your exams.
 * Two students side by side, both giving a thumbs-up, with celebratory
 * stars and spark marks. */
const { C, W, sh, fl, ln, dot, limbUnder, limbOver, coilyHair } = require('./_kit');

module.exports = function scene() {
  const teeB = '#2F5A8C', teeBShade = '#22436B';
  const teeG = '#F2B23C', teeGShade = '#D8912A';
  const strap = '#8A6E4E', pack = '#2C3542';

  const star = (x, y, r, fill) => {
    const pts = Array.from({ length: 10 }, (_, i) => {
      const rr = i % 2 ? r * 0.46 : r;
      const a = (Math.PI / 5) * i - Math.PI / 2;
      return `${(x + rr * Math.cos(a)).toFixed(1)} ${(y + rr * Math.sin(a)).toFixed(1)}`;
    }).join(' L ');
    return `<path d="M ${pts} Z" fill="${fill}" stroke="${C.outline}" stroke-width="2.6" stroke-linejoin="round"/>`;
  };

  const ground = `
    ${fl('M 0 1000 L 0 806 Q 116 728 296 748 Q 470 770 520 884 Q 548 946 540 1000 Z', C.blueBlob)}
    ${star(158, 578, 44, C.gold)}
    ${star(892, 116, 40, C.gold)}
    ${ln('M 494 104 L 520 168', 11, '#E08A2E')}
    ${ln('M 542 100 L 552 162', 11, '#E08A2E')}
    ${ln('M 806 92 L 782 148', 11, '#E08A2E')}`;

  /* --- the two students ------------------------------------------------------- */
  const armB = 'M 452 706 Q 452 622 502 574';
  const armG = 'M 902 762 Q 880 690 902 646';

  const boy = `
    ${limbUnder('M 668 372 L 672 418', 64)}
    ${limbOver('M 668 372 L 672 418', 64, C.skinShade)}
    ${fl('M 300 700 Q 268 748 268 830 L 268 940 Q 300 962 350 950 L 356 720 Z', pack)}
    ${sh('M 592 268 Q 586 190 660 176 Q 740 170 756 246 Q 770 334 726 378 Q 678 418 634 390 Q 598 356 592 268 Z', C.skin)}
    ${fl('M 712 192 Q 756 220 754 286 Q 758 348 726 378 Q 746 310 738 252 Q 730 210 712 192 Z', C.skinLit)}
    ${coilyHair(674, 250, 92, 82, { bumps: 12, from: 198, to: -18, brow: 0.42 })}

    ${ln('M 610 274 Q 632 262 654 272', 3.8)}
    ${ln('M 692 270 Q 712 258 732 270', 3.8)}
    ${dot(632, 300, 12, C.outline)}${dot(712, 296, 12, C.outline)}
    ${ln('M 664 302 Q 660 336 674 348 Q 664 356 652 350', 3)}
    ${sh('M 626 366 Q 668 396 712 364 Q 702 406 668 408 Q 636 406 626 366 Z', C.white, W.detail)}
    ${ln('M 626 366 Q 668 380 712 364', 3)}
    ${dot(608, 342, 12, '#C97A4A')}${dot(736, 336, 12, '#C97A4A')}

    ${sh('M 340 1000 Q 336 616 404 532 Q 456 470 546 458 L 662 464 Q 742 492 762 596 Q 786 796 788 1000 Z', teeB)}
    ${fl('M 682 476 Q 748 520 764 616 Q 786 810 788 1000 L 706 1000 Q 724 728 682 476 Z', teeBShade)}
    ${ln('M 578 470 Q 626 532 700 512', 3, teeBShade)}
    ${sh('M 542 524 Q 500 610 486 722 Q 476 838 486 1000 L 400 1000 Q 388 806 408 674 Q 428 578 470 518 Z', strap)}
    ${sh('M 286 690 Q 356 662 396 700 Q 420 760 414 852 Q 408 946 380 1000 L 268 1000 Q 250 900 254 800 Q 258 720 286 690 Z', pack)}
    ${fl('M 340 676 Q 400 690 412 766 Q 420 872 386 1000 L 340 1000 Q 372 840 340 676 Z', '#20272F')}

    ${limbUnder(armB, 64)}${limbOver(armB, 64, C.skin)}
    ${sh('M 468 500 Q 508 476 552 496 Q 592 520 584 566 Q 570 616 512 620 Q 456 618 440 584 Q 430 536 468 500 Z', C.skin)}
    ${sh('M 470 500 Q 456 444 480 412 Q 506 388 526 410 Q 542 438 528 500 Z', C.skin)}
    ${ln('M 460 540 Q 502 534 542 548', 2.8, C.skinShade)}
    ${ln('M 462 574 Q 502 570 540 582', 2.8, C.skinShade)}`;

  const girl = `
    ${limbUnder('M 876 398 L 880 444', 60)}
    ${limbOver('M 876 398 L 880 444', 60, C.skinShade)}
    ${[[796, 264, -1], [806, 232, -1], [956, 240, 1], [966, 272, 1], [982, 316, 1]].map(([x, y, s2]) => {
      const d = `M ${x} ${y} C ${x + s2 * 34} ${y + 90} ${x + s2 * 12} ${y + 170} ${x + s2 * 40} ${y + 248}`;
      return `<path d="${d}" fill="none" stroke="${C.outline}" stroke-width="23" stroke-linecap="round"/>` +
             `<path d="${d}" fill="none" stroke="${C.hair}" stroke-width="18" stroke-linecap="round"/>`;
    }).join('')}

    ${sh('M 800 288 Q 794 214 866 200 Q 942 194 958 268 Q 972 352 930 394 Q 884 432 842 406 Q 806 372 800 288 Z', C.skin)}
    ${fl('M 916 216 Q 958 244 956 306 Q 960 364 930 394 Q 948 330 940 274 Q 932 234 916 216 Z', C.skinLit)}
    ${sh('M 796 278 Q 782 202 862 188 Q 944 182 962 244 Q 972 296 952 308 Q 942 240 890 226 Q 826 222 810 278 Z', C.hair, W.hair)}

    ${ln('M 816 294 Q 838 282 858 292', 3.8)}
    ${ln('M 894 288 Q 914 276 934 288', 3.8)}
    ${dot(838, 318, 11, C.outline)}${dot(914, 314, 11, C.outline)}
    ${ln('M 872 320 Q 868 350 882 362 Q 872 370 860 364', 3)}
    ${sh('M 834 380 Q 874 408 914 378 Q 904 418 872 420 Q 842 418 834 380 Z', C.white, W.detail)}
    ${ln('M 834 380 Q 874 394 914 378', 3)}
    ${dot(814, 356, 11, '#C97A4A')}${dot(940, 350, 11, '#C97A4A')}

    ${sh('M 754 1000 Q 750 644 812 570 Q 858 512 934 502 L 1002 506 L 1002 1000 Z', teeG)}
    ${fl('M 944 506 Q 1000 532 1002 622 L 1002 1000 L 930 1000 Q 954 728 944 506 Z', teeGShade)}
    ${ln('M 836 542 Q 884 602 950 582', 3, teeGShade)}
    ${sh('M 930 504 Q 890 586 878 688 Q 870 818 878 1000 L 812 1000 Q 802 796 818 656 Q 836 548 872 508 Z', strap)}

    ${sh('M 916 548 L 1002 542 L 1002 934 L 922 942 Z', '#2C5180')}
    ${fl('M 916 548 L 950 546 L 954 938 L 922 942 Z', '#1F3E64')}

    ${limbUnder(armG, 60)}${limbOver(armG, 60, C.skin)}
    ${sh('M 848 730 Q 886 708 926 726 Q 962 748 954 790 Q 940 836 886 840 Q 836 838 822 806 Q 814 762 848 730 Z', C.skin)}
    ${sh('M 850 730 Q 838 678 860 650 Q 884 628 902 648 Q 916 674 904 730 Z', C.skin)}
    ${ln('M 840 766 Q 880 760 916 774', 2.8, C.skinShade)}
    ${ln('M 842 798 Q 880 794 914 806', 2.8, C.skinShade)}`;

  return ground + boy + girl;
};
