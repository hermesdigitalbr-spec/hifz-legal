#!/usr/bin/env python3
"""Generates the static legal pages for Hifz (CSS inline). Usage: python3 build.py"""
import pathlib
ROOT = pathlib.Path(__file__).parent
MAIL = '<a href="mailto:support@hermes.com.br">support@hermes.com.br</a>'
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
UPDATED = "Last updated: November 10, 2026"
CSS = """
:root{--ground:#F5EEDF;--surface:#FBF6EA;--ink:#1E2A3A;--navy:#1E3557;--gold:#7D5E26;--text2:#3A4556;
--hair:rgba(30,53,87,.18);--serif:"Iowan Old Style","Palatino Linotype",Georgia,serif;
--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);font-size:16.5px;line-height:1.62;-webkit-font-smoothing:antialiased}
.top{background:var(--navy);color:#F5EEDF;text-align:center;padding:42px 22px 30px}
.top .ar{font-family:"Geeza Pro","Amiri",serif;font-size:26px;color:#D4B26A}
.top h1{font-family:var(--serif);font-weight:500;font-size:clamp(30px,7vw,40px);margin:6px 0 6px;line-height:1.1}
.top p{margin:0;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:#D4B26A}
.strip{height:14px;background:repeating-conic-gradient(from 45deg,#B08A3E 0 25%,#F5EEDF 0 50%);background-size:14px 14px}
.wrap{max-width:40rem;margin:0 auto;padding:10px 22px 80px}
h2{font-family:var(--serif);font-size:21px;font-weight:600;margin:34px 0 8px;color:var(--navy)}
p,li{color:var(--text2);margin:0 0 .85rem}ul{padding-left:1.15rem}li::marker{color:#B08A3E}
strong{color:var(--ink)}a{color:var(--navy);text-underline-offset:2px}
.card{background:var(--surface);border:1px solid #B08A3E;padding:18px 20px;margin:24px 0}
.docs{list-style:none;padding:0}.docs li{border-top:1px solid var(--hair);margin:0}.docs li:first-child{border-top:0}
.docs a{display:block;padding:15px 2px;text-decoration:none;font-family:var(--serif);font-size:18px}
footer{margin-top:48px;padding-top:18px;border-top:1px solid var(--hair);font-size:13px;color:#4A5568;text-align:center}
footer a{color:#4A5568}
"""
def page(slug, title, body):
    foot = "" if slug == "index" else ' · <a href="./">Legal documents</a>'
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Hifz</title><style>{CSS}</style></head>
<body><div class="top"><div class="ar">حِفْظ</div><h1>{title}</h1><p>Hifz · Qur'an memorization</p></div><div class="strip"></div>
<main class="wrap"><p style="font-size:13px;color:#4A5568;margin-top:18px">{UPDATED}</p>{body}
<footer>Hifz is published by Hermes Digital · {MAIL}{foot}</footer></main></body></html>"""
    (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")

page("index", "Legal documents", """
<p>Hifz helps you memorize the Qur'an with the madrasa method (Sabaq, Sabqi and Manzil) and spaced repetition.</p>
<ul class="docs"><li><a href="terms">Terms of Use</a></li><li><a href="privacy">Privacy Policy</a></li><li><a href="support">Support</a></li></ul>""")

page("terms", "Terms of Use", f"""
<p>These terms govern your use of the Hifz app for iPhone and iPad ("the app"), published by Hermes Digital. By using the app you agree to them and to Apple's <a href="{EULA}">Standard End User License Agreement</a>, which applies in full.</p>
<h2>The service</h2>
<p>Hifz schedules your daily memorization: a new lesson (Sabaq), daily revision of recent lessons (Sabqi) and spaced revision of older portions (Manzil). Schedules, strength estimates and certificates are study aids. They are not an ijazah and do not replace a qualified teacher.</p>
<h2>Hifz Plus subscriptions</h2>
<ul>
<li>Hifz Plus is offered as an auto-renewable subscription, yearly or monthly. Prices are shown in the app in your local currency before you buy.</li>
<li>The yearly plan may include a free trial. If you do not cancel at least 24 hours before the trial ends, the subscription starts and your Apple ID is charged the yearly price.</li>
<li>Payment is charged to your Apple ID at confirmation of purchase (or at the end of the trial). Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period. Your account is charged for renewal within 24 hours before the end of the period.</li>
<li>You can manage or cancel your subscription in your Apple ID settings (Settings › your name › Subscriptions) or from Settings › Account in the app. Unused time of a free trial is forfeited when you buy a subscription.</li>
<li>Refunds are handled by Apple under its policies.</li>
</ul>
<h2>Free access on request</h2>
<p>If you cannot afford Hifz Plus, you may ask for free access at {MAIL}. Requests are granted at our discretion using App Store offer codes.</p>
<h2>Content and attributions</h2>
<p>The Qur'an text is from the Tanzil Project (tanzil.net), used under the Creative Commons Attribution 3.0 license and shown without modification. The English translation is by Marmaduke Pickthall (1930, public domain). Recitation audio is streamed from EveryAyah.com. These sources belong to their owners; Hifz does not claim them.</p>
<h2>Acceptable use</h2>
<p>Do not misuse the app, reverse engineer it, or use it to break any law. Recordings you make and share are your responsibility.</p>
<h2>Liability</h2>
<p>The app is provided "as is". To the extent allowed by law, Hermes Digital is not liable for indirect or consequential damages arising from its use.</p>
<h2>Changes</h2>
<p>We may update these terms; the date above shows the latest version. Continued use after a change means you accept it.</p>
<h2>Contact</h2><p>{MAIL}</p>""")

page("privacy", "Privacy Policy", f"""
<div class="card"><p><strong>In short:</strong> Hifz does not collect your personal data. Your plan, progress, slips and recordings stay on your device, and, if you sign in with Apple, in your own iCloud account. There are no ads, no analytics and no tracking.</p></div>
<h2>What stays on your device</h2>
<ul>
<li><strong>Your memorization record</strong>: plan, lessons, revision schedule, slip log, sittings, teacher notes and halaqa details.</li>
<li><strong>Recordings</strong> of your recitation, made only when you press record. They never leave your device unless you share them yourself (for example with your teacher) through the share sheet.</li>
<li><strong>Approximate location</strong>, only if you allow it, rounded to about 1 km and used on the device to calculate prayer times for your reminder. It is never sent anywhere.</li>
</ul>
<h2>Sign in with Apple and iCloud</h2>
<p>Signing in is optional. If you sign in with Apple, the app receives an anonymous identifier and, if you choose to share them, your name and email. With iCloud backup on, a copy of your record is stored in your private iCloud key-value storage so it can be restored on a new device. We cannot see it.</p>
<h2>Purchases</h2>
<p>Subscriptions are processed by Apple. We do not receive your payment details. Apple shares anonymous, aggregated sales reports with developers.</p>
<h2>Third-party content</h2>
<p>When you play recitation, the audio files are downloaded from EveryAyah.com (and word-by-word audio from the Quran.com content network). As with any web request, those servers can see your IP address. No account or personal data is sent.</p>
<h2>Notifications and microphone</h2>
<p>Reminders are local notifications scheduled on your device. Microphone access is used only while you record.</p>
<h2>Children</h2><p>Hifz is suitable for all ages and does not knowingly collect data from anyone.</p>
<h2>Deleting your data</h2>
<p>Settings › Account › Delete account erases everything on the device and in your iCloud backup. Deleting the app also removes the data stored on the device. You can export your record first (Settings › Account › Export my data).</p>
<h2>Contact</h2><p>{MAIL}</p>""")

page("support", "Support", f"""
<p>Questions, a problem with a lesson, or a mistake in a screen? Write to {MAIL}. We answer in English, Portuguese and Spanish.</p>
<h2>Frequent questions</h2>
<p><strong>How do I cancel my subscription?</strong> Settings › your name › Subscriptions on your iPhone, or Settings › Account › Manage subscription in Hifz.</p>
<p><strong>I changed phones. How do I keep my progress?</strong> Sign in with Apple and keep iCloud backup on (Settings › Account). On the new phone, choose "I already have an account".</p>
<p><strong>Audio does not play.</strong> Recitation streams from the internet. Download the surahs you need in Listen › Downloads to use them offline.</p>
<p><strong>Can I get free access?</strong> If you cannot afford Hifz Plus, write to us. We give free access codes on request.</p>
<p><strong>Is a Hifz certificate an ijazah?</strong> No. Certificates record facts (what you recited, when, and who listened). An ijazah comes only from a qualified teacher.</p>
<h2>Credits</h2>
<p>Qur'an text: Tanzil Project (CC BY 3.0). Translation: M. Pickthall (public domain). Audio: EveryAyah.com. Prayer times: Adhan library (MIT). Fonts: Amiri, Amiri Quran, Scheherazade New and Cormorant Garamond (SIL Open Font License).</p>""")
print("ok")
