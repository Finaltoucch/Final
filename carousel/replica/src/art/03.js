/* 03 — Get adequate sleep.
 * Student asleep under a duvet, night window above the bed, digital clock
 * reading 10:30 PM on the nightstand. */
const { C, W, sh, fl, ln, dot, label, coilyHair } = require('./_kit');

module.exports = function scene() {
  const duvet = '#22406A', duvetShade = '#1A3355';
  const tee = '#3C6394';
  const night = '#152B45';

  const ground = `
    ${fl('M 1002 96 Q 872 116 830 214 Q 792 306 700 350 Q 604 396 592 500 Q 582 610 664 668 L 1002 668 Z', C.blueBlobLt)}
    ${fl('M 1002 168 Q 900 196 866 274 Q 832 352 754 392 Q 676 432 668 512 Q 662 594 726 640 L 1002 640 Z', C.blueBlob)}`;

  /* --- night window ----------------------------------------------------- */
  const stars = [[832, 246], [944, 236], [858, 342], [934, 314], [896, 380]]
    .map(([x, y], i) => (i % 2
      ? dot(x, y, 4.5, '#F2CE72')
      : `<path d="M ${x} ${y - 9} L ${x + 3} ${y - 3} L ${x + 9} ${y} L ${x + 3} ${y + 3} L ${x} ${y + 9} ` +
        `L ${x - 3} ${y + 3} L ${x - 9} ${y} L ${x - 3} ${y - 3} Z" fill="#F2CE72"/>`)).join('');

  const window_ = `
    ${sh('M 795 130 L 974 138 L 966 406 L 803 400 Z', night, 9)}
    ${fl('M 812 152 L 958 158 L 951 386 L 819 381 Z', '#1B3557')}
    ${sh('M 900 186 Q 856 190 850 228 Q 846 268 886 276 Q 852 262 856 226 Q 862 194 900 186 Z', '#F0C75E', 0)}
    ${stars}`;

  const zees = `
    ${label(700, 372, 'z', 52, C.navy, 900)}
    ${label(752, 330, 'Z', 62, C.navy, 900)}`;

  /* --- bed -------------------------------------------------------------- */
  const bed = `
    ${sh('M 336 806 Q 336 764 392 762 L 1002 762 L 1002 940 L 336 940 Z', '#F2EAD6')}
    ${ln('M 348 830 L 1002 830', 2.4, '#DCD0B4')}
    ${sh('M 402 462 Q 396 418 456 412 L 690 420 Q 736 430 730 484 L 726 690 Q 720 726 668 722 L 452 706 Q 404 700 404 656 Z', '#2C5180')}
    ${fl('M 640 430 Q 720 448 722 508 L 718 690 Q 712 720 668 718 L 596 712 Q 674 620 660 508 Z', '#24446E')}`;

  /* --- the sleeper ------------------------------------------------------- */
  const figure = `
    ${sh('M 486 512 Q 470 430 556 406 Q 660 392 692 470 Q 720 556 668 604 Q 604 648 542 622 Q 494 592 486 512 Z', C.skin)}
    ${fl('M 636 424 Q 700 456 700 528 Q 700 588 660 610 Q 686 540 672 480 Q 660 440 636 424 Z', C.skinLit)}
    ${coilyHair(576, 486, 108, 100, { bumps: 12, from: 226, to: 34, brow: 0.30 })}

    ${ln('M 520 528 Q 546 516 568 526', 3.4)}
    ${ln('M 604 528 Q 628 518 648 530', 3.4)}
    ${ln('M 522 556 Q 546 570 570 556', 3.4)}
    ${ln('M 606 556 Q 628 570 650 556', 3.4)}
    ${ln('M 588 556 Q 584 586 600 596 Q 590 604 578 598', 2.8)}
    ${ln('M 566 620 Q 592 634 620 618', 3.2)}

    ${sh('M 640 640 Q 760 636 812 700 Q 862 764 866 830 L 700 830 Q 668 742 620 700 Z', tee)}
    ${sh('M 1002 700 Q 900 674 800 700 Q 700 728 636 800 Q 596 848 590 940 L 1002 940 Z', duvet)}
    ${fl('M 1002 754 Q 900 748 826 792 Q 736 846 716 940 L 1002 940 Z', duvetShade)}
    ${ln('M 962 786 Q 866 806 806 866', 3, duvetShade)}
    ${ln('M 1000 852 Q 928 866 884 916', 3, duvetShade)}

    ${sh('M 560 690 Q 606 660 656 676 Q 700 696 690 736 Q 676 776 620 780 Q 564 780 546 750 Q 536 714 560 690 Z', C.skin)}
    ${ln('M 588 692 Q 626 690 654 706', 2.6, C.skinShade)}
    ${ln('M 580 720 Q 622 716 658 732', 2.6, C.skinShade)}
    ${ln('M 584 748 Q 618 746 646 756', 2.6, C.skinShade)}`;

  /* --- nightstand and clock ---------------------------------------------- */
  const digit = (x, y, s, text, fill) =>
    `<text x="${x}" y="${y}" font-family="Lato" font-size="${s}" font-weight="900" fill="${fill}" text-anchor="middle" letter-spacing="1">${text}</text>`;

  const stand = `
    ${sh('M 74 862 L 452 862 L 442 906 L 84 906 Z', C.woodLit)}
    ${fl('M 74 892 L 452 892 L 448 906 L 78 906 Z', C.woodDark)}
    ${sh('M 100 906 L 428 906 L 424 1000 L 104 1000 Z', C.wood)}
    ${ln('M 112 950 L 414 950', 2.4, C.woodDark)}

    ${sh('M 156 738 L 372 738 Q 386 738 386 752 L 386 848 Q 386 862 372 862 L 156 862 Q 142 862 142 848 L 142 752 Q 142 738 156 738 Z', '#282A2E')}
    ${fl('M 166 758 L 362 758 L 362 842 L 166 842 Z', '#3A3D42')}
    ${digit(264, 818, 62, '10:30', '#F2EFE6')}
    ${digit(264, 856, 26, 'PM', '#F2EFE6')}`;

  void W;
  return ground + window_ + zees + bed + figure + stand;
};
