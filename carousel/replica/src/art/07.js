/* 07 — Students with established medical conditions.
 * Student reading a MEDICAL ADVICE sheet, with a medication carton, a bottle
 * and a blister pack laid out on the table. */
const { C, W, sh, fl, ln, dot, label, sprig, limbUnder, limbOver, coilyHair } = require('./_kit');

module.exports = function scene() {
  const knit = '#6E8C64', knitShade = '#587353';

  const ground = `
    ${fl('M 470 412 Q 506 334 578 356 Q 636 378 632 442 Q 690 470 674 540 Q 654 610 570 596 Q 512 634 466 592 Q 424 546 452 490 Q 440 442 470 412 Z', '#D7DEE4')}
    ${sprig(96, 1000, 1.15, -10, C.greenLeaf, C.greenDeep)}
    ${sprig(22, 968, 0.9, 18, C.olive, C.greenDeep)}`;

  /* --- the student ----------------------------------------------------------- */
  const armNear = 'M 946 706 Q 872 690 812 650';
  const armFar = 'M 1002 566 Q 934 552 880 578';

  const figure = `
    ${limbUnder('M 812 380 L 818 470', 62)}
    ${limbOver('M 812 380 L 818 470', 62, C.skinShade)}
    ${sh('M 728 268 Q 722 186 802 170 Q 890 164 906 248 Q 920 344 872 390 Q 820 432 774 402 Q 734 364 728 268 Z', C.skin)}
    ${fl('M 858 186 Q 906 216 904 288 Q 908 356 872 388 Q 894 314 886 252 Q 878 206 858 186 Z', C.skinLit)}
    ${sh('M 722 286 Q 700 282 702 306 Q 704 332 728 332', C.skin, W.detail)}
    ${coilyHair(816, 254, 104, 96, { bumps: 13, from: 202, to: -22, brow: 0.40 })}

    ${ln('M 748 292 Q 772 278 796 290', 3.8)}
    ${ln('M 830 286 Q 852 274 874 288', 3.8)}
    ${fl('M 752 318 Q 774 306 796 320 Q 774 330 752 318 Z', C.outline)}
    ${fl('M 832 314 Q 854 302 874 316 Q 854 326 832 314 Z', C.outline)}
    ${ln('M 812 320 Q 808 356 824 370 Q 812 378 800 372', 3)}
    ${ln('M 786 396 Q 812 388 838 398', 3.2)}

    ${sh('M 690 1000 Q 686 764 756 686 Q 806 630 878 626 L 1002 632 L 1002 1000 Z', knit)}
    ${fl('M 906 632 Q 1000 660 1002 754 L 1002 1000 L 912 1000 Q 936 800 906 632 Z', knitShade)}
    ${ln('M 782 690 Q 838 748 912 726', 3, knitShade)}
    ${limbUnder(armFar, 62)}${limbOver(armFar, 62, knit)}`;

  /* --- the advice sheet ------------------------------------------------------- */
  const sheet = `
    <g transform="translate(46 40) scale(0.86) rotate(-7 726 620)">
      ${sh('M 560 452 L 878 452 Q 892 452 892 466 L 892 762 Q 892 776 878 776 L 560 776 Q 546 776 546 762 L 546 466 Q 546 452 560 452 Z', '#F7F4EA')}
      ${fl('M 806 452 L 878 452 Q 892 452 892 466 L 892 762 Q 892 776 878 776 L 806 776 Z', '#EAE5D6')}
      ${label(714, 546, 'MEDICAL', 46, C.outline, 900, 'letter-spacing="1.4"')}
      ${label(714, 602, 'ADVICE', 46, C.outline, 900, 'letter-spacing="1.4"')}
      ${ln('M 578 646 L 862 646', 3, '#C9C2AE')}
      ${ln('M 578 682 L 862 682', 3, '#C9C2AE')}
      ${ln('M 578 718 L 780 718', 3, '#C9C2AE')}
    </g>`;

  const nearHand = `
    ${limbUnder(armNear, 60)}${limbOver(armNear, 60, knit)}
    ${sh('M 754 616 Q 796 596 838 616 Q 870 640 850 668 Q 806 692 766 672 Q 738 646 754 616 Z', C.skin)}
    ${ln('M 780 618 Q 816 618 840 634', 2.8, C.skinShade)}
    ${ln('M 772 644 Q 810 642 844 656', 2.8, C.skinShade)}
    ${ln('M 776 668 Q 806 668 832 678', 2.8, C.skinShade)}`;

  /* --- table ------------------------------------------------------------------- */
  const table = `
    ${sh('M 226 1000 Q 220 830 424 792 Q 690 758 1002 766 L 1002 1000 Z', C.woodLit)}
    ${fl('M 248 918 Q 400 872 660 862 Q 850 858 1002 864 L 1002 1000 L 244 1000 Z', C.wood)}
    ${ln('M 314 848 Q 620 806 1000 806', 2.4, C.woodDark)}`;

  /* --- medication ---------------------------------------------------------------- */
  const carton = `
    ${sh('M 356 836 L 584 812 L 584 950 L 356 974 Z', '#E4E7EA')}
    ${fl('M 356 836 L 584 812 L 584 850 L 356 874 Z', '#F2F4F6')}
    ${sh('M 382 884 L 562 866 L 562 922 L 382 940 Z', '#F7F8F9')}
    ${label(472, 914, 'MEDICATION', 28, C.outline, 900, 'letter-spacing="0.8"')}`;

  const bottle = `
    ${sh('M 478 706 L 564 706 L 572 866 Q 574 888 552 890 L 492 890 Q 470 888 472 866 Z', '#CBDDEA')}
    ${fl('M 536 710 L 564 710 L 572 866 Q 574 886 554 888 L 526 888 Q 546 794 536 710 Z', '#B4CCE0')}
    ${sh('M 488 666 L 554 666 L 556 706 L 486 706 Z', '#DCE8F1')}
    ${sh('M 484 640 L 558 640 L 556 670 L 486 670 Z', '#3F7048')}
    ${fl('M 472 806 L 572 806 L 572 882 L 472 882 Z', '#9EBED6')}`;

  const blister = `
    <g transform="rotate(-4 726 858)">
      ${sh('M 614 802 L 842 802 Q 854 802 854 814 L 854 904 Q 854 916 842 916 L 614 916 Q 602 916 602 904 L 602 814 Q 602 802 614 802 Z', '#C9CFD4')}
      ${[0, 1, 2].map(c => [0, 1].map(r =>
        `<circle cx="${664 + c * 78}" cy="${836 + r * 46}" r="21" fill="#F5EDDD" stroke="${C.outline}" stroke-width="2.6"/>` +
        `<circle cx="${664 + c * 78}" cy="${836 + r * 46}" r="12" fill="#E8A33C"/>`).join('')).join('')}
    </g>`;

  void W; void dot;
  return ground + figure + sheet + nearHand + table + bottle + carton + blister;
};
