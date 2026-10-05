# THE LAST GOODBYE — DELIVERY RECORD
Delivered 5 October 2026. Track: ALEXATOR "012 Last Goodbye".

## THE THREE FILES
| # | File | Size | Checksum |
|---|---|---|---|
| 01 | `01_FINAL_ALEXATOR_LAST_GOODBYE.mp4` | 73,780,540 B | MD5 `ee944e0eb6c35ce9acc9bff65980941c` |
| 02 | `02_USED_AI_SOURCES.zip` | 323,045,493 B | SHA-256 `57de76e3024176b560e1dcedacad41242825d9a1e909d526921a892408d077e6` |
| 03 | `03_ORIGIN_PROOF.zip` (holds the PDF) | 53,845 B | PDF SHA-256 `9640a8cf0bee61f0343c91162db38a68f418268ea98980a0ee15ef9c1c2e9ec1` |

Hosted:
- film `https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/e7110a8c-d9bf-491d-8417-7fde4de393ac.mp4`
- sources `https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/0ca5b0fe-a0e3-48ab-a824-391423854ced.zip`
- proof `https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/a6923e4a-fcab-46dc-aec6-be2eda003b12.zip`

## VERIFICATION ON THE DELIVERED FILE
```
1080x1920   DAR 9:16   24 fps   1338 frames   55.754 s
audio AAC 48 kHz stereo 320k, 55.750 s
blackdetect    none
freezedetect   none
cropdetect     1080:1920:0:0
ebur128        -13.7 LUFS - LRA 1.2 LU - true peak -3.3 dBFS
cuts measured  84 168 252 335 460 585 710 835 960 1086 1212
cuts planned   84 168 252 335 460 585 710 835 960 1086 1212   <- all eleven matched
```
First film of the three where every scene cut was detected exactly on plan.

## CLIENT NOTE APPLIED BEFORE THE SHOT LIST, NOT AFTER
Out-point 176.246800 s is the bar line where the post-drop 24-bar phrase
resolves. The drop sits on frame 335 (the near-touch of the two hands) and the
remaining 24 bars play out to completion, so the climax is not cut short.

## FINAL CLIP IDS
| # | frames | clip job |
|---|---|---|
| 01 | 0–83 | `5475778a-6ba3-49af-a690-3817623c08dc` |
| 02 | 84–167 | `ddf44572-c289-4840-a643-a63e92cc4c91` |
| 03 | 168–251 | `1e25aae1-05df-4263-8ab3-fbdae1b04caa` |
| 04 | 252–334 | `977c8b4a-26e2-4224-907c-000926fbad07` |
| 05 | 335–459 | `ee4f9b9b-25bd-41ea-bacf-6bbad0496a67` |
| 06 | 460–584 | `20db29b7-33bc-46af-9771-db34068786ed` |
| 07 | 585–709 | `a7dad20c-ed02-4766-9db1-bc562810d05d` |
| 08 | 710–834 | `bf1049e9-fe76-4414-9615-6767f285dd42` |
| 09 | 835–959 | `75706b00-b35c-4d07-8a0f-15e64d35ca6e` |
| 10 | 960–1085 | `7400f9f8-dc23-44d0-a066-d0680dee7d28` |
| 11 | 1086–1211 | `f98d5ddf-c057-4c84-8ad4-9f399f267021` |
| 12 | 1212–1337 | `02feb349-b935-40d0-93c8-340d5be2057d` |

Final keyframes for shots 10 and 11 are the v2 images
`8de708f6-4797-49d0-8144-cc8f8aca89c8` and `0da8b078-be1b-41c1-8e82-3f226938e108`;
the bible's table lists the superseded v1s.

## DISCLOSED CHOICE — SHOT 10
Shot 09 puts the queen in a large ceremonial collar; shot 10 does not carry it.
Three versions were generated. v3 had the collar right but turned the servant
into a pole-bearer who never looks at her, which is the whole point of the shot.
v2 was chosen and the collar discrepancy accepted knowingly. Stated to the
client in the manifest rather than hidden.

## SPEND
| Item | Credits |
|---|---|
| stills (6 plates, 12 keyframes, redos) | ~54.00 |
| 4 clips @ 7.50 | 30.00 |
| 8 clips @ 9.00 | 72.00 |
| shot 10 / 11 keyframe redos | ~6.00 |
| **total** | **~162.00** |

Balance 605.58 -> 443.58 (verified). Three backend failures cost nothing
(shot 08 twice on weapon-adjacent wording, shot 11 once on "clenched hard /
knuckles pale with force").

## STILL OUTSTANDING — NEEDS THE LOGGED-IN ACCOUNT
The origin proof PDF carries a boxed page listing six items only the account
holder can produce: four commercial-use term URLs, four account screenshots,
and signature plus date. Same six are outstanding on DESCENT.

## NEW LESSON FOR THE PLAYBOOK
`sandbox_exec` **refuses** a command that embeds a large base64 blob — it blocks
relaying file bytes as text across environments. Anything the sandbox needs must
arrive by URL (curl) or be written by a command that fits the 16,000-char limit.
So verbatim prompt dumps cannot be shipped into the sandbox; put the provenance
table and the locked specs in the manifest instead, written inline by heredoc.
