/* 09 — Sign-off.
 * Heart with an ECG trace and radiating marks on the deep navy ground, with
 * foliage in both bottom corners. The wording itself is set in HTML. */
const { C, ln, fl, sprig } = require('./_kit');

module.exports = function scene() {
  const red = '#D4553A';
  const gold = '#F0C243';

  const heart = `
    ${fl('M 500 336 Q 386 250 386 176 Q 386 112 442 108 Q 486 108 500 152 Q 514 108 558 108 Q 614 112 614 176 Q 614 250 500 336 Z', red)}
    <path d="M 398 202 L 452 202 L 468 174 L 486 246 L 512 132 L 532 208 L 548 186 L 602 186"
          fill="none" stroke="${gold}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>`;

  const rays = [
    'M 288 190 L 350 208', 'M 300 244 L 356 244', 'M 296 300 L 352 278',
    'M 712 190 L 650 208', 'M 700 244 L 644 244', 'M 704 300 L 648 278',
  ].map(d => ln(d, 8, gold)).join('');

  const foliage = `
    ${sprig(-16, 1000, 1.95, -14, '#3E6693', '#2C5180')}
    ${sprig(86, 1024, 1.7, 18, '#6E8C64', '#4F7346')}
    ${sprig(1018, 1010, 1.95, 20, '#6E8C64', '#4F7346')}
    ${sprig(918, 1028, 1.65, -14, '#4F7346', '#3E5B3C')}`;

  void C;
  return foliage + rays + heart;
};
