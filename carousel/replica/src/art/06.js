/* 06 — Seek medical attention early.
 * Student with a headache in the foreground, the Medical Center behind her. */
const { C, W, sh, fl, ln, dot, label, limbUnder, limbOver } = require('./_kit');

module.exports = function scene() {
  const tee = '#2F5A8C', teeShade = '#22436B';
  const wall = '#EAE4D6', wallShade = '#D8D1C0';
  const roof = '#3F4A46';

  const ground = `
    ${fl('M 96 606 Q 62 522 148 486 Q 226 458 286 502 Q 352 470 402 522 Q 462 586 396 640 L 120 646 Z', C.blueBlobLt)}
    ${fl('M 690 470 Q 662 396 738 366 Q 812 342 866 386 Q 932 358 976 408 Q 1030 470 968 520 L 720 526 Z', C.blueBlobLt)}
    ${dot(652, 150, 15, '#7FA2C6')}
    ${dot(608, 246, 14, '#E8A33C')}`;

  /* --- the Medical Center --------------------------------------------------- */
  const building = `
    ${sh('M 150 700 L 300 700 L 300 890 L 150 890 Z', wallShade)}
    ${sh('M 620 704 L 800 704 L 800 890 L 620 890 Z', wallShade)}
    ${ln('M 210 726 L 210 780', 3, C.greyDeep)}${ln('M 240 726 L 240 780', 3, C.greyDeep)}
    ${ln('M 660 730 L 660 800', 3, C.greyDeep)}${ln('M 700 730 L 700 800', 3, C.greyDeep)}

    ${sh('M 276 610 L 414 528 L 552 610 L 552 890 L 276 890 Z', wall)}
    ${sh('M 258 620 L 414 528 L 570 620 L 552 638 L 414 556 L 276 638 Z', roof)}
    ${fl('M 470 566 L 552 614 L 552 890 L 470 890 Z', wallShade)}

    ${sh('M 386 636 L 442 636 L 442 664 L 470 664 L 470 720 L 442 720 L 442 748 L 386 748 L 386 720 L 358 720 L 358 664 L 386 664 Z', '#2F5A8C')}
    ${label(414, 800, 'MEDICAL', 41, C.outline, 900, 'letter-spacing="1.2"')}
    ${label(414, 846, 'CENTER', 41, C.outline, 900, 'letter-spacing="1.2"')}

    ${sh('M 306 862 L 522 862 L 534 890 L 294 890 Z', '#2F5A8C')}
    ${sh('M 330 890 L 498 890 L 498 1000 L 330 1000 Z', '#2C4D74')}
    ${ln('M 414 890 L 414 1000', 3.4, '#1D3450')}
    ${fl('M 340 900 L 406 900 L 406 990 L 340 990 Z', '#3E6693')}
    ${fl('M 422 900 L 488 900 L 488 990 L 422 990 Z', '#3E6693')}`;

  const bushes = `
    ${fl('M 0 992 L 0 880 Q 60 848 122 880 Q 176 910 176 992 Z', C.greenDeep)}
    ${fl('M 138 992 Q 146 906 210 894 Q 274 890 288 992 Z', C.greenLeaf)}
    ${fl('M 528 992 Q 538 902 606 892 Q 672 892 682 992 Z', C.greenLeaf)}
    ${fl('M 664 992 Q 676 916 736 906 Q 796 906 806 992 Z', C.greenDeep)}
    ${fl('M 0 978 L 1002 978 L 1002 1000 L 0 1000 Z', '#E7E0CE')}`;

  /* --- the student ---------------------------------------------------------- */
  const armHead = 'M 828 660 Q 750 600 736 494 Q 732 424 774 372';

  const figure = `
    ${limbUnder('M 864 460 L 868 528', 58)}
    ${limbOver('M 864 460 L 868 528', 58, C.skinShade)}
    ${sh('M 742 1000 Q 736 754 802 684 Q 852 630 922 626 L 1002 632 L 1002 1000 Z', tee)}
    ${fl('M 932 630 Q 1000 658 1002 744 L 1002 1000 L 926 1000 Q 950 772 932 630 Z', teeShade)}
    ${ln('M 824 668 Q 874 720 942 700', 3, teeShade)}

    ${sh('M 774 356 Q 766 274 846 258 Q 930 252 948 336 Q 962 430 916 476 Q 864 518 818 490 Q 780 452 774 356 Z', C.skin)}
    ${fl('M 900 274 Q 948 304 946 376 Q 950 444 914 476 Q 936 402 928 340 Q 920 294 900 274 Z', C.skinLit)}
    ${sh('M 768 372 Q 748 368 750 392 Q 752 416 774 416', C.skin, W.detail)}

    ${sh('M 772 344 Q 758 254 846 238 Q 936 230 954 300 Q 964 356 942 368 Q 930 292 872 278 Q 802 274 786 344 Z', C.hair, W.hair)}
    ${sh('M 872 234 Q 828 208 856 176 Q 894 150 934 178 Q 972 208 934 240 Q 904 258 872 234 Z', C.hair, W.hair)}
    ${ln('M 866 194 Q 892 182 918 200', 3, C.hairLit)}
    ${ln('M 860 216 Q 890 202 922 220', 3, C.hairLit)}

    ${ln('M 794 372 Q 818 356 842 368', 3.8)}
    ${ln('M 880 364 Q 902 352 922 364', 3.8)}
    ${ln('M 796 398 Q 818 412 842 398', 3.6)}
    ${ln('M 882 392 Q 902 406 922 392', 3.6)}
    ${ln('M 862 396 Q 858 428 872 440 Q 862 448 850 442', 3)}
    ${ln('M 836 466 Q 862 456 888 468', 3.2)}

    ${limbUnder(armHead, 62)}
    ${limbOver(armHead, 62, C.skin)}
    ${sh('M 770 296 Q 806 268 852 280 Q 892 296 886 334 Q 874 376 828 380 Q 778 378 762 352 Q 752 318 770 296 Z', C.skin)}
    ${ln('M 790 288 Q 828 280 856 296', 3, C.skinShade)}
    ${ln('M 778 318 Q 818 310 856 326', 3, C.skinShade)}
    ${ln('M 778 350 Q 812 344 842 356', 3, C.skinShade)}`;

  void W;
  return ground + building + bushes + figure;
};
