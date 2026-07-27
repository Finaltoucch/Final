/* 02 — Take study breaks.
 * Student standing beside her desk mid side-stretch: wall clock behind, desk
 * lamp and a small pot on the desk, chair pushed back, tall plant right. */
const { C, W, sh, fl, ln, circ, dot, label, limbUnder, limbOver } = require('./_kit');

module.exports = function scene() {
  const tee = '#F2B23C', teeShade = '#D8912A';
  const denim = '#22406A', denimShade = '#1A3355';

  const ground = `
    ${fl('M0 690 Q 64 668 104 716 Q 140 764 110 812 Q 84 856 118 900 L 0 900 Z', C.blueBlob)}
    ${fl('M0 934 L 1002 934 L 1002 1000 L 0 1000 Z', '#F6EEDD')}
    ${ln('M 0 934 L 1002 934', 2.4, '#E4D9C2')}`;

  /* --- wall clock ------------------------------------------------------ */
  const ticks = Array.from({ length: 12 }, (_, i) => {
    const a = (i * 30 * Math.PI) / 180;
    const [x1, y1] = [509 + 56 * Math.sin(a), 505 - 56 * Math.cos(a)];
    const [x2, y2] = [509 + 46 * Math.sin(a), 505 - 46 * Math.cos(a)];
    return ln(`M ${x1.toFixed(1)} ${y1.toFixed(1)} L ${x2.toFixed(1)} ${y2.toFixed(1)}`, 3, C.navyLine);
  }).join('');

  const clock = `
    ${circ(509, 505, 71, '#F7F1E1', 7).replace(`stroke="${C.outline}"`, `stroke="${C.navyLine}"`)}
    ${ticks}
    ${ln('M 509 505 L 509 455', 5, C.navyLine)}
    ${ln('M 509 505 L 548 528', 5, C.navyLine)}
    ${dot(509, 505, 6, C.navyLine)}`;

  /* --- desk, lamp, pot -------------------------------------------------- */
  const desk = `
    ${sh('M 176 752 L 640 752 L 622 800 L 194 800 Z', C.woodLit)}
    ${fl('M 176 786 L 640 786 L 634 800 L 182 800 Z', C.woodDark)}
    ${sh('M 210 800 L 226 800 L 236 934 L 216 934 Z', C.wood)}
    ${sh('M 600 800 L 616 800 L 610 934 L 590 934 Z', C.wood)}`;

  const lamp = `
    ${sh('M 286 786 Q 286 764 336 764 Q 386 764 386 786 Q 386 796 336 796 Q 286 796 286 786 Z', C.navyLine)}
    ${ln('M 316 770 L 344 660', 8, C.navyLine)}
    ${ln('M 344 660 L 396 606', 8, C.navyLine)}
    ${sh('M 372 570 Q 430 556 452 606 Q 462 632 452 646 L 372 660 Q 356 632 372 570 Z', C.navyLine)}
    ${fl('M 396 646 Q 424 640 448 646 Q 428 664 396 646 Z', '#FBEFCB')}
    ${fl('M 400 664 Q 420 700 414 760 Q 404 704 394 668 Z', '#F8E3AE', 'opacity=".8"')}
    ${dot(322, 662, 9, C.navyLine)}`;

  const pot = `
    ${sh('M 478 700 Q 500 656 512 640 Q 522 660 516 700 Z', C.greenLeaf)}
    ${sh('M 516 698 Q 546 660 566 650 Q 566 678 540 702 Z', C.greenLeaf)}
    ${sh('M 480 702 Q 456 672 448 654 Q 476 656 496 692 Z', C.greenLeaf)}
    ${sh('M 470 702 L 556 702 L 544 762 Q 542 770 532 770 L 494 770 Q 484 770 482 762 Z', '#C9743A')}
    ${ln('M 476 720 L 550 720', 3, C.woodDark)}`;

  const chair = `
    ${sh('M 62 746 Q 62 726 84 726 L 296 726 Q 318 726 318 748 L 318 890 Q 318 910 296 910 L 84 910 Q 62 910 62 890 Z', '#2B4A6E')}
    ${fl('M 250 730 Q 314 736 314 800 L 314 900 L 262 906 Q 276 800 250 730 Z', denimShade)}
    ${sh('M 78 906 L 96 906 L 104 1000 L 82 1000 Z', C.navyLine)}
    ${sh('M 296 906 L 314 906 L 306 1000 L 284 1000 Z', C.navyLine)}`;

  /* --- tall plant on the right ------------------------------------------ */
  const blade = (d) => sh(d, C.greenLeaf, W.detail);
  const plant = `
    ${blade('M 930 690 Q 892 560 906 470 Q 940 556 946 690 Z')}
    ${blade('M 942 692 Q 962 540 1004 470 Q 1006 590 972 692 Z')}
    ${blade('M 922 700 Q 862 636 846 566 Q 908 606 940 700 Z')}
    ${blade('M 950 700 Q 1002 636 1004 588 Q 1006 660 972 704 Z')}
    ${blade('M 934 704 Q 894 700 858 664 Q 908 668 946 706 Z')}
    ${sh('M 862 704 L 1004 704 L 986 906 Q 984 920 970 920 L 894 920 Q 880 920 878 906 Z', '#C9743A')}
    ${fl('M 950 706 L 1002 706 L 984 906 Q 982 918 970 918 L 936 918 Q 962 812 950 706 Z', '#B15E2D')}
    ${ln('M 868 744 L 998 744', 4, C.woodDark)}`;

  /* --- the student ------------------------------------------------------ */
  const legL = 'M 660 892 Q 700 760 726 620';
  const legR = 'M 828 892 Q 800 760 780 620';
  const armUp = 'M 812 396 Q 874 300 846 208 Q 820 134 736 116';
  const armHip = 'M 692 404 Q 626 466 640 528 Q 654 578 716 578';

  const legs = `
    ${limbUnder(legL, 66)}${limbUnder(legR, 66)}
    ${limbOver(legL, 66, denim)}${limbOver(legR, 66, denim)}
    ${ln('M 634 886 Q 674 756 700 620', 8, '#F2EEE4')}
    ${fl('M 812 700 Q 828 780 838 880 L 806 886 Q 798 782 786 704 Z', denimShade)}
    ${sh('M 610 886 Q 654 872 690 886 Q 710 900 704 918 L 600 918 Q 588 900 610 886 Z', '#F2EEE4')}
    ${sh('M 790 886 Q 834 872 870 886 Q 890 900 884 918 L 780 918 Q 768 900 790 886 Z', '#F2EEE4')}
    ${ln('M 604 906 L 700 906', 2.2, C.grey)}
    ${ln('M 784 906 L 880 906', 2.2, C.grey)}`;

  const arm = `
    ${limbUnder(armUp, 44)}
    ${limbOver(armUp, 44, C.skin)}
    ${sh('M 736 92 Q 698 84 682 108 Q 670 134 694 144 Q 728 152 746 130 Q 756 106 736 92 Z', C.skin)}
    ${ln('M 694 112 L 718 106', 2.4, C.skinShade)}
    ${ln('M 698 126 L 724 120', 2.4, C.skinShade)}`;

  const torso = `
    ${sh('M 700 412 Q 706 356 748 344 L 800 348 Q 842 372 838 436 Q 834 528 812 608 Q 754 630 700 604 Q 694 508 700 412 Z', tee)}
    ${fl('M 786 352 Q 838 380 834 448 Q 830 530 812 608 L 768 620 Q 800 508 796 412 Z', teeShade)}
    ${ln('M 744 352 Q 764 384 794 372', 3, teeShade)}
    ${ln('M 718 470 Q 758 490 802 476', 2.4, teeShade)}`;

  const hipArm = `
    ${limbUnder(armHip, 44)}
    ${limbOver(armHip, 44, C.skin)}
    ${sh('M 704 556 Q 738 550 754 568 Q 764 588 742 596 Q 708 602 694 586 Q 688 566 704 556 Z', C.skin)}`;

  const head = `
    ${sh('M 664 268 Q 660 202 714 190 Q 776 188 786 250 Q 796 318 760 340 Q 722 358 694 336 Q 666 314 664 268 Z', C.skin)}
    ${fl('M 744 202 Q 786 222 784 272 Q 788 320 760 340 Q 772 290 766 248 Q 760 216 744 202 Z', C.skinLit)}
    ${sh('M 658 288 Q 638 284 640 306 Q 642 328 664 328', C.skin, W.detail)}

    ${sh('M 662 264 Q 646 196 712 182 Q 782 176 794 238 Q 800 280 784 292 Q 776 230 726 218 Q 680 214 662 264 Z', C.hair, W.hair)}
    ${sh('M 754 168 Q 716 146 740 118 Q 772 96 806 118 Q 838 144 806 170 Q 782 188 754 168 Z', C.hair, W.hair)}
    ${ln('M 764 130 Q 786 120 806 136', 3, C.hairLit)}
    ${ln('M 756 150 Q 782 138 810 154', 3, C.hairLit)}

    ${ln('M 670 290 Q 686 282 702 290', 3.4)}
    ${ln('M 728 286 Q 744 278 758 288', 3.4)}
    ${ln('M 672 310 Q 688 320 704 310', 3.2)}
    ${ln('M 730 308 Q 746 318 760 308', 3.2)}
    ${ln('M 712 308 Q 708 330 720 338', 2.6)}
    ${ln('M 700 354 Q 720 364 740 352', 3)}`;

  const figure = legs + arm + torso + hipArm + head;

  void label; void dot;
  return ground + clock + chair + desk + lamp + pot + plant + figure;
};
