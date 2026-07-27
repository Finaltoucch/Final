/* 04 — Eat proper meals and stay hydrated.
 * Student eating a bowl of vegetables at a table, water bottle and fruit
 * alongside; long braids, warm sand-coloured wash behind. */
const { C, W, sh, fl, ln, dot, sprig, limbUnder, limbOver } = require('./_kit');

module.exports = function scene() {
  const tee = '#7C8A50', teeShade = '#667440';

  const ground = `
    ${fl('M 1002 78 Q 836 96 772 202 Q 712 306 616 380 Q 508 462 514 590 Q 520 718 646 772 L 1002 772 Z', '#F7E7C6')}
    ${dot(648, 143, 17, '#F3C777')}
    ${dot(611, 257, 13, '#F3C777')}
    ${dot(157, 872, 12, '#7FA2C6')}
    ${sprig(70, 990, 1.0, -8, C.olive, C.greenDeep)}
    ${sprig(20, 962, 0.8, 20, C.greenLeaf, C.greenDeep)}`;

  /* --- braids, hanging clear of the face ---------------------------------- */
  const braid = (x, y, len, sway) => {
    const d = `M ${x} ${y} C ${x + sway * 3} ${y + len * 0.3} ${x + sway * 6} ${y + len * 0.55} ` +
      `${x + sway * 4} ${y + len * 0.78} S ${x + sway * 1.5} ${y + len} ${x + sway * 3} ${y + len}`;
    return `<path d="${d}" fill="none" stroke="${C.outline}" stroke-width="20" stroke-linecap="round"/>` +
      `<path d="${d}" fill="none" stroke="${C.hair}" stroke-width="15" stroke-linecap="round"/>`;
  };

  const braids = [
    braid(688, 268, 300, -8), braid(702, 240, 330, -6), braid(722, 218, 300, -5),
    braid(880, 214, 330, 5), braid(898, 240, 300, 6), braid(908, 274, 260, 8),
  ].join('');

  /* --- table --------------------------------------------------------------- */
  const table = `
    ${sh('M 268 1000 Q 262 812 452 768 Q 692 736 1002 744 L 1002 1000 Z', C.woodLit)}
    ${fl('M 292 918 Q 430 884 668 872 Q 852 866 1002 872 L 1002 1000 L 288 1000 Z', C.wood)}
    ${ln('M 348 812 Q 620 780 1000 782', 2.4, C.woodDark)}`;

  /* --- the student ---------------------------------------------------------- */
  const armSpoon = 'M 744 800 Q 668 720 626 618 Q 604 566 604 534';

  const figure = `
    ${braids}
    ${sh('M 593 1000 Q 588 762 652 690 Q 700 640 762 634 L 852 638 Q 950 664 968 748 Q 1000 850 1002 1000 Z', tee)}
    ${fl('M 872 646 Q 966 686 980 780 Q 1000 880 1002 1000 L 916 1000 Q 930 812 872 646 Z', teeShade)}
    ${ln('M 752 646 Q 792 700 850 686 Q 878 678 886 648', 3, teeShade)}

    ${sh('M 704 300 Q 698 226 768 210 Q 850 204 866 284 Q 880 374 836 420 Q 786 460 740 432 Q 706 396 704 300 Z', C.skin)}
    ${fl('M 818 226 Q 866 254 864 324 Q 868 390 834 420 Q 854 350 846 290 Q 838 246 818 226 Z', C.skinLit)}
    ${sh('M 698 316 Q 678 312 680 336 Q 682 360 704 360', C.skin, W.detail)}

    ${sh('M 694 296 Q 678 212 762 194 Q 856 186 876 262 Q 888 318 866 330 Q 856 258 800 240 Q 732 232 710 296 Z', C.hair, W.hair)}
    ${ln('M 718 226 Q 778 198 842 226', 3.4, C.hairLit)}
    ${ln('M 712 250 Q 780 218 852 252', 3.4, C.hairLit)}

    ${ln('M 716 320 Q 738 308 758 318', 3.6)}
    ${ln('M 794 314 Q 814 304 834 316', 3.6)}
    ${fl('M 720 342 Q 740 332 758 344 Q 740 352 720 342 Z', C.outline)}
    ${fl('M 796 338 Q 814 328 834 340 Q 814 348 796 338 Z', C.outline)}
    ${ln('M 774 346 Q 770 376 784 388 Q 774 396 762 390', 3)}
    ${ln('M 752 410 Q 778 422 802 408', 3.2)}
    ${dot(726, 380, 11, '#C97A4A')}${dot(842, 370, 11, '#C97A4A')}

    ${limbUnder(armSpoon, 52)}
    ${limbOver(armSpoon, 52, C.skin)}
    ${sh('M 570 496 Q 610 480 644 500 Q 672 524 650 546 Q 610 566 578 546 Q 554 522 570 496 Z', C.skin)}
    ${ln('M 594 502 Q 624 502 646 518', 2.4, C.skinShade)}
    ${ln('M 588 528 Q 618 528 642 540', 2.4, C.skinShade)}
    ${ln('M 640 508 L 690 490', 7, C.grey)}
    ${sh('M 668 470 Q 704 466 712 490 Q 718 514 690 520 Q 660 522 654 498 Q 652 478 668 470 Z', '#D8D5CD')}
    ${dot(684, 494, 13, '#E2A24C')}`;

  /* --- bottle, bowl, fruit --------------------------------------------------- */
  const bottle = `
    ${sh('M 470 668 L 544 668 L 554 848 Q 556 874 530 876 L 484 876 Q 458 874 460 848 Z', '#CFE0EC')}
    ${fl('M 520 672 L 544 672 L 552 848 Q 554 872 534 874 L 508 874 Q 530 774 520 672 Z', '#B9D0E2')}
    ${sh('M 478 620 L 536 620 L 540 668 L 474 668 Z', '#D8E6F0')}
    ${sh('M 472 594 L 542 594 L 540 624 L 474 624 Z', '#2C5180')}
    ${ln('M 468 712 L 550 712', 2.2, '#9FBBD2')}
    ${ln('M 464 782 L 554 782', 2.2, '#9FBBD2')}`;

  const veg = [
    [644, 748, 20, C.greenLeaf], [692, 736, 18, '#C9743A'], [742, 744, 20, C.greenLeaf],
    [790, 736, 17, '#C9743A'], [836, 746, 19, '#8AA05A'], [668, 766, 16, '#8AA05A'],
    [720, 768, 18, '#C9743A'], [768, 766, 16, C.greenLeaf], [814, 768, 15, '#8AA05A'],
  ].map(([x, y, r, f]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${f}" stroke="${C.outline}" stroke-width="2.4"/>`).join('');

  const bowl = `
    ${sh('M 602 752 Q 606 764 620 770 Q 736 792 858 768 Q 868 762 870 752 Q 736 726 602 752 Z', '#EAE5D8')}
    ${veg}
    ${sh('M 602 752 Q 606 830 736 838 Q 866 830 870 752 Q 800 786 736 786 Q 672 786 602 752 Z', '#F6F3EA')}
    ${sh('M 700 842 L 776 842 L 770 858 L 706 858 Z', '#E6E1D3')}`;

  const fruit = `
    ${sh('M 738 892 Q 746 842 802 830 Q 866 822 874 856 Q 878 894 818 906 Q 766 910 738 892 Z', '#F0C243')}
    ${ln('M 756 884 Q 804 854 856 850', 2.4, '#D8A22A')}
    ${sh('M 872 832 Q 906 806 942 826 Q 966 846 958 878 Q 942 910 904 908 Q 868 902 864 868 Q 862 846 872 832 Z', '#C8402C')}
    ${fl('M 910 820 Q 944 826 954 856 Q 960 886 936 904 Q 956 858 910 820 Z', '#A62F20')}
    ${ln('M 906 820 Q 912 802 928 796', 4, C.greenDeep)}`;

  return ground + figure + table + bottle + bowl + fruit;
};
