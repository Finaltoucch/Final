/* Copy and per-panel typography for the nine replica cards.
 *
 * Sizes are in the 1000-unit design space; the renderer scales the whole card
 * to whatever pixel size is asked for, so these never change with output size.
 *
 * `measure` is the body column width. Body copy is stored as running text and
 * wrapped by the browser — the measure is set so it breaks on the same words
 * the source does, which keeps the copy editable instead of hard-broken.
 */

module.exports = [
  {
    n: 1, slug: '01-study-targets',
    heading: ['Set realistic', 'study targets.'],
    headSize: 85, headLead: 0.98,
    body: ['Work for one academic-session cannot be forced into your brain in one night.'],
    bodySize: 37, bodyLead: 1.36, measure: 340, bodyTop: 404,
  },
  {
    n: 2, slug: '02-study-breaks',
    heading: ['Take', 'study breaks.'],
    headSize: 88, headLead: 0.97,
    body: ['Do not sit in one place for too long. Stretch your legs, rest your eyes, and refresh your mind.'],
    bodySize: 37, bodyLead: 1.36, measure: 372, bodyTop: 404,
  },
  {
    n: 3, slug: '03-sleep',
    heading: ['Get adequate', 'sleep.'],
    headSize: 88, headLead: 0.97,
    body: ['Avoid regular all night studying. Sleep is important for memory consolidation and concentration.'],
    bodySize: 37, bodyLead: 1.36, measure: 300, bodyTop: 404,
  },
  {
    n: 4, slug: '04-meals-hydration',
    heading: ['Eat proper meals', 'and stay hydrated.'],
    headSize: 71, headLead: 1.02, headTop: 174,
    body: [
      'Do not rely on junk food. Your brain and entire body need adequate energy from balanced diets during stressful periods. Adequate water intake can reduce headaches and poor concentration.',
      'Do not skip breakfast on the day of an exam.',
    ],
    bodySize: 35, bodyLead: 1.34, measure: 410, bodyTop: 322, paraGap: 30,
  },
  {
    n: 5, slug: '05-no-quick-fixes',
    heading: ['Avoid performance', 'enhancers and', 'quick fixes.'],
    headSize: 68, headLead: 1.02, headTop: 178,
    body: ['Do not use energy drinks, drugs or alcohol to manage stress or stay alert. Avoid excessive caffeine (eg coffee) intake. They can cause anxiety, insomnia, energy crashes (drop in physical and mental alertness).'],
    bodySize: 34, bodyLead: 1.33, measure: 392, bodyTop: 396,
  },
  {
    n: 6, slug: '06-seek-care-early',
    heading: ['Seek medical', 'attention early.'],
    headSize: 76, headLead: 1.0, headTop: 192,
    body: ['Visit the Medical Center as soon as you detect a decline in your health.'],
    bodySize: 35, bodyLead: 1.36, measure: 372, bodyTop: 360,
  },
  {
    n: 7, slug: '07-existing-conditions',
    heading: [], badge: 92,
    body: ['Students with established medical conditions should ensure that their medications are fully stocked. They should also adhere to all medical advices concerning their condition. If you feel the sitting arrangements in the examination hall would aggravate your condition, kindly inform the examiner on time.'],
    bodySize: 36, bodyLead: 1.34, measure: 430, bodyTop: 166,
  },
  {
    n: 8, slug: '08-well-wishes',
    heading: ['We wish you', 'all the best in', 'your exams.'],
    headSize: 70, headLead: 1.06, headTop: 178,
    body: [],
  },
  {
    n: 9, slug: '09-signoff',
    ground: 'navy',
    signoff: { lead: 'The medical team,', name: ['Nnamdi Azikiwe', 'University Medical Center,'], place: 'Awka.' },
  },
];
