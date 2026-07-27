/* 05 — Avoid performance enhancers and quick fixes.
 * Student in a red hoodie refusing a coffee cup, energy drink and bottle
 * lined up on the table; a red cross-mark seals the refusal. */
const { C, W, sh, fl, ln, dot, label, limbUnder, limbOver, coilyHair } = require('./_kit');

module.exports = function scene() {
  const hood = '#9E3A2A', hoodShade = '#7C2A1D';

  const ground = `
    ${dot(1004, 214, 26, '#BFD3E6')}
    ${dot(996, 300, 13, '#BFD3E6')}`;

  /* --- the student -------------------------------------------------------- */
  const armStop = 'M 830 566 Q 872 596 872 660';

  const figure = `
    ${limbUnder('M 712 424 L 716 520', 62)}
    ${limbOver('M 712 424 L 716 520', 62, C.skinShade)}
    ${sh('M 632 320 Q 626 244 700 230 Q 782 224 798 302 Q 812 392 768 436 Q 718 476 674 448 Q 638 412 632 320 Z', C.skin)}
    ${fl('M 752 246 Q 798 274 796 342 Q 800 406 766 436 Q 786 366 778 306 Q 770 264 752 246 Z', C.skinLit)}
    ${sh('M 626 336 Q 606 332 608 356 Q 610 380 632 380', C.skin, W.detail)}
    ${coilyHair(716, 306, 96, 88, { bumps: 12, from: 200, to: -20, brow: 0.40 })}

    ${ln('M 646 340 Q 668 328 690 338', 3.8)}
    ${ln('M 722 336 Q 744 326 764 338', 3.8)}
    ${fl('M 650 364 Q 670 354 690 366 Q 670 376 650 364 Z', C.outline)}
    ${fl('M 724 362 Q 744 352 762 364 Q 744 372 724 362 Z', C.outline)}
    ${ln('M 704 368 Q 700 402 714 414 Q 704 422 692 416', 3)}
    ${ln('M 684 442 Q 706 434 728 442', 3.2)}

    ${limbUnder(armStop, 60)}
    ${limbOver(armStop, 60, C.skin)}
    ${sh('M 566 1000 Q 560 728 620 640 Q 664 566 742 552 L 812 556 Q 892 584 912 668 Q 940 800 942 1000 Z', hood)}
    ${fl('M 828 566 Q 898 606 916 692 Q 940 812 942 1000 L 862 1000 Q 878 776 828 566 Z', hoodShade)}
    ${sh('M 676 548 Q 728 596 796 578 Q 828 566 838 544 Q 800 520 736 522 Q 690 526 676 548 Z', hoodShade)}
    ${fl('M 722 566 Q 748 578 776 574 L 774 604 Q 744 610 722 598 Z', '#E0A63C')}
    ${ln('M 714 588 Q 706 660 714 704', 6, hoodShade)}
    ${ln('M 762 590 Q 772 660 764 704', 6, hoodShade)}
    ${dot(714, 710, 10, hoodShade)}${dot(764, 710, 10, hoodShade)}

    ${sh('M 774 652 Q 772 602 798 598 Q 822 596 826 640 L 832 666 Z', C.skin, W.detail)}
    ${sh('M 818 646 Q 816 588 844 584 Q 868 584 870 638 L 872 668 Z', C.skin, W.detail)}
    ${sh('M 862 652 Q 862 604 888 602 Q 910 604 910 650 L 908 678 Z', C.skin, W.detail)}
    ${sh('M 902 670 Q 904 628 926 628 Q 946 632 942 674 L 938 698 Z', C.skin, W.detail)}
    ${sh('M 764 706 Q 754 646 782 640 L 916 652 Q 944 666 936 722 Q 924 788 854 796 Q 788 792 772 744 Z', C.skin)}
    ${sh('M 766 712 Q 736 688 726 706 Q 718 730 746 754 L 774 760 Z', C.skin, W.detail)}
    ${ln('M 788 718 Q 842 712 898 722', 2.8, C.skinShade)}`;

  /* --- table --------------------------------------------------------------- */
  const table = `
    ${sh('M 1002 690 L 462 774 Q 366 794 322 878 L 274 1000 L 1002 1000 Z', C.woodLit)}
    ${fl('M 1002 848 L 468 896 Q 396 906 366 954 L 344 1000 L 1002 1000 Z', C.wood)}
    ${ln('M 986 748 L 512 814', 2.2, C.woodDark)}
    ${ln('M 986 804 L 462 872', 2.2, C.woodDark)}`;

  /* --- what is being refused ------------------------------------------------ */
  const cup = `
    ${sh('M 470 686 L 610 686 L 590 900 Q 588 916 572 916 L 508 916 Q 492 916 490 900 Z', '#F7F3E9')}
    ${fl('M 566 690 L 610 690 L 590 900 Q 588 914 574 914 L 550 914 Q 574 800 566 690 Z', '#E7E1D2')}
    ${sh('M 458 650 L 622 650 Q 632 650 632 662 L 628 686 Q 626 696 616 696 L 464 696 Q 454 696 452 686 L 450 662 Q 450 650 458 650 Z', '#3A2A20')}
    ${label(540, 806, 'COFFEE', 32, C.outline, 900, 'letter-spacing="1"')}`;

  const can = `
    ${sh('M 640 748 L 736 748 L 728 932 Q 726 946 712 946 L 664 946 Q 650 946 648 932 Z', '#22406A')}
    ${fl('M 706 750 L 736 750 L 728 932 Q 726 944 714 944 L 694 944 Q 712 850 706 750 Z', '#182F4F')}
    ${sh('M 640 736 L 736 736 L 736 750 L 640 750 Z', '#C9C6BE')}
    ${label(688, 836, 'ENERGY', 27, C.white, 900)}
    ${label(688, 866, 'DRINK', 27, C.white, 900)}`;

  const bottle = `
    ${sh('M 776 706 L 826 706 L 828 764 Q 862 796 866 856 L 868 926 Q 868 944 850 944 L 754 944 Q 736 944 736 926 L 738 856 Q 742 796 774 764 Z', '#B87A22')}
    ${fl('M 812 712 L 826 712 L 828 766 Q 860 798 864 858 L 866 926 Q 866 942 850 942 L 816 942 Q 838 850 830 770 Q 826 736 812 712 Z', '#96601A')}
    ${sh('M 774 664 L 828 664 L 828 710 L 774 710 Z', '#6E4A16')}
    ${fl('M 752 806 L 800 806 L 800 900 L 752 900 Z', '#D8A44A')}`;

  const cross = `
    ${dot(352, 906, 68, '#C8402C')}
    ${ln('M 322 876 L 382 936', 17, C.white)}
    ${ln('M 382 876 L 322 936', 17, C.white)}`;

  return ground + figure + table + cup + can + bottle + cross;
};
