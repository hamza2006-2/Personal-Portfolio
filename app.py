
from flask import Flask, render_template_string, send_from_directory, request
from pathlib import Path
import csv
from datetime import datetime

app = Flask(__name__)
BASE = Path(__file__).resolve().parent
IMAGE = BASE / "hamza.jpg.jpeg"
CONTACTS = BASE / "inquiries.csv"

GITHUB = "https://github.com/hamza2006-2"
EMAIL = "iamhamza.ahmed0008@gmail.com"

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Hamza Ahmed — Developer, Data Science Student and E-commerce Specialist.">
<title>Hamza Ahmed | Developer & Digital Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
 --bg:#080a12;--panel:#111522;--white:#f5f5fb;
 --muted:#9ba5b8;--purple:#b49aff;--cyan:#69dded;
 --line:rgba(255,255,255,.09);--green:#c6f27a;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:85px}
body{background:var(--bg);color:var(--white);font-family:'DM Sans',sans-serif;line-height:1.7}
a{text-decoration:none;color:inherit}
button,input,textarea{font:inherit}
.container{width:min(1160px,90%);margin:auto}
body:before{
 content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
 background:radial-gradient(ellipse at 10% 15%,#6646a52b,transparent 38%),
 radial-gradient(ellipse at 90% 45%,#238ca522,transparent 35%);
}
header{position:fixed;top:0;width:100%;z-index:10;
 background:#080a12d9;backdrop-filter:blur(18px);
 border-bottom:1px solid var(--line)}
nav{height:76px;display:flex;align-items:center;justify-content:space-between}
.logo{font:800 24px Manrope;letter-spacing:-1px}
.logo span{color:var(--purple)}
.links{display:flex;align-items:center;gap:27px;font-size:13px;color:#c4cada}
.links a:hover{color:var(--cyan)}
.navbtn{border:1px solid #a78bfa88;padding:9px 16px;border-radius:30px}
.menu{display:none;background:none;color:white;border:0;font-size:26px}
.hero{min-height:760px;padding:150px 0 95px;display:flex;align-items:center}
.hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:65px;align-items:center}
.tag{display:inline-block;border:1px solid #a78bfa55;background:#a78bfa12;color:#d3c5ff;border-radius:30px;padding:7px 14px;font-size:11px;letter-spacing:1.5px;text-transform:uppercase}
.tag:before{content:"●";color:var(--green);margin-right:9px}
h1,h2,h3,.logo{font-family:Manrope,sans-serif}
h1{font-size:clamp(48px,6vw,78px);line-height:1.08;letter-spacing:-4px;margin:25px 0}
.gradient{background:linear-gradient(110deg,#c5aaff,#70dced);color:transparent;background-clip:text}
.role{font-size:20px;font-weight:600;margin-bottom:15px}
.description{color:var(--muted);max-width:600px;font-size:15px;line-height:2}
.actions{display:flex;gap:13px;flex-wrap:wrap;margin-top:28px}
.btn{display:inline-block;padding:12px 19px;border-radius:9px;font-size:13px;font-weight:700;transition:.25s}
.btn:hover{transform:translateY(-3px)}
.primary{background:linear-gradient(110deg,#c7adff,#75dcec);color:#10111b}
.outline{border:1px solid var(--line);background:#ffffff08}
.social{display:flex;gap:22px;flex-wrap:wrap;margin-top:27px;font-size:13px;color:#d5dbea}
.social a:hover{color:var(--cyan)}
.portrait{position:relative;width:330px;height:420px;margin:auto;padding:4px;
 background:linear-gradient(140deg,#c5aaff,#6cdbea);
 border-radius:25px;box-shadow:0 25px 100px #0009}
.portrait img{width:100%;height:100%;object-fit:cover;border-radius:22px;background:#171b28}
.photo-label{position:absolute;bottom:20px;left:-28px;padding:13px 19px;
 background:#151a29ed;border:1px solid var(--line);border-radius:12px;font-size:12px}
.photo-label strong{display:block;font:700 15px Manrope}
.section{padding:100px 0}
.heading{margin-bottom:38px}
.eyebrow{color:var(--cyan);font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:700}
.heading h2{font-size:clamp(32px,4vw,46px);letter-spacing:-2px;line-height:1.2;margin:12px 0}
.heading p{color:var(--muted);font-size:14px}
.about-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:45px}
.copy{color:var(--muted);font-size:15px;line-height:2}
.copy p{margin-bottom:15px}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.fact,.card{background:linear-gradient(140deg,#151a29,#101420);
 border:1px solid var(--line);border-radius:15px;padding:22px}
.fact strong{display:block;font:700 16px Manrope}
.fact span{font-size:12px;color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}
.card{transition:.25s}
.card:hover{transform:translateY(-5px);border-color:#8cbbdc88}
.card-icon{font-size:25px;margin-bottom:13px}
.card h3{font-size:17px;margin-bottom:9px}
.card p{font-size:13px;color:var(--muted);line-height:1.9}
.skills{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.skill{padding:15px;background:#111522;border:1px solid var(--line);
 border-radius:10px;font-size:13px;color:#e2e5ef}
.skill span{margin-right:9px}
.project-number{font-size:11px;color:var(--cyan);letter-spacing:2px}
.project-tag{display:inline-block;margin-top:17px;background:#a78bfa17;
 color:#c9b8ff;border-radius:30px;padding:5px 10px;font-size:10px}
.contact-box{max-width:760px;background:var(--panel);padding:28px;
 border:1px solid var(--line);border-radius:16px}
.field{width:100%;background:#090d17;border:1px solid var(--line);
 color:white;padding:14px;border-radius:9px;margin-bottom:13px;outline:none}
.field:focus{border-color:var(--purple)}
textarea.field{min-height:125px;resize:vertical}
.contact-links{display:flex;gap:20px;flex-wrap:wrap;margin-top:20px;font-size:13px}
.contact-links a{color:var(--cyan)}
.success{color:var(--green);margin-bottom:15px;font-size:13px}
footer{padding:28px 0;border-top:1px solid var(--line);color:var(--muted);font-size:12px}
.footer-row{display:flex;justify-content:space-between;gap:15px;flex-wrap:wrap}
footer a{color:var(--purple)}
.reveal{opacity:0;transform:translateY(15px);transition:.7s}
.reveal.show{opacity:1;transform:none}
@media(max-width:800px){
 .hero-grid{gap:35px}.portrait{width:270px;height:350px}
 .grid{grid-template-columns:repeat(2,1fr)}
 .skills{grid-template-columns:repeat(3,1fr)}
}
@media(max-width:620px){
 .menu{display:block}
 .links{display:none;position:absolute;top:76px;left:0;width:100%;
 background:#111522;padding:25px;flex-direction:column}
 .links.open{display:flex}
 .hero{padding:120px 0 70px}
 .hero-grid{grid-template-columns:1fr;text-align:center}
 .portrait{width:245px;height:315px}
 .description{margin:auto}
 .actions,.social{justify-content:center}
 h1{letter-spacing:-2px}
 .section{padding:70px 0}
 .about-grid{grid-template-columns:1fr}
 .grid{grid-template-columns:1fr}
 .skills{grid-template-columns:repeat(2,1fr)}
 .heading{text-align:center}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
</style>
</head>
<body>
<header>
<nav class="container">
<a href="#home" class="logo">HAMZA<span>.</span></a>
<button class="menu" onclick="document.querySelector('.links').classList.toggle('open')">☰</button>
<div class="links">
<a href="#home">Home</a><a href="#about">About</a>
<a href="#skills">Skills</a><a href="#experience">Experience</a>
<a href="#projects">Projects</a><a href="#contact" class="navbtn">Contact ↗</a>
</div>
</nav>
</header>

<main>
<section class="hero" id="home">
<div class="container hero-grid">
<div>
<div class="tag">Developer · Learner · Builder</div>
<h1>Turning ideas<br>into <span class="gradient">reality.</span></h1>
<div class="role">Hamza Ahmed | Developer & Data Science Student</div>
<p class="description">I enjoy building digital experiences, exploring data and solving practical problems through technology. My interests span software development, analytics and e-commerce.</p>
<div class="actions">
<a class="btn primary" href="#projects">Explore my work ↗</a>
<a class="btn outline" href="mailto:iamhamza.ahmed0008@gmail.com?subject=Hello%20Hamza">Let's talk ↗</a>
</div>
<div class="social">
<a href="https://github.com/hamza2006-2" target="_blank" rel="noopener">⌘ GitHub profile ↗</a>
<a href="mailto:iamhamza.ahmed0008@gmail.com">✉ iamhamza.ahmed0008@gmail.com ↗</a>
</div>
</div>
<div class="portrait">
<img src="/profile-image" alt="Hamza Ahmed profile photo">
<div class="photo-label"><strong>Hamza Ahmed</strong>Learning. Building. Growing.</div>
</div>
</div>
</section>

<section class="section" id="about">
<div class="container">
<div class="heading"><div class="eyebrow">01 / About me</div>
<h2>Curiosity drives <span class="gradient">progress.</span></h2>
<p>A little about my background and what I enjoy doing.</p></div>
<div class="about-grid">
<div class="copy">
<p>I'm a technology enthusiast focused on software development, data science and digital business. I enjoy learning by building, experimenting with ideas and improving my skills through practical work.</p>
<p>Alongside development, I have experience with e-commerce research, Amazon product sourcing, supplier discovery, marketplace operations and business data research.</p>
<p>I'm interested in meaningful projects, collaborations and opportunities where I can contribute, learn and grow.</p>
</div>
<div class="facts">
<div class="fact"><strong>Development</strong><span>Python, Flask and web technologies</span></div>
<div class="fact"><strong>Data</strong><span>Analysis and business research</span></div>
<div class="fact"><strong>E-commerce</strong><span>Amazon and Shopify workflows</span></div>
<div class="fact"><strong>Learning</strong><span>MERN and Flutter development</span></div>
</div>
</div>
</div>
</section>

<section class="section" id="skills">
<div class="container">
<div class="heading"><div class="eyebrow">02 / My toolkit</div>
<h2>Skills & <span class="gradient">technologies.</span></h2>
<p>Tools and areas I'm working with and developing further.</p></div>
<div class="skills">
<div class="skill">🐍 Python</div><div class="skill">🔥 Flask</div>
<div class="skill">🌐 HTML & CSS</div><div class="skill">⚡ JavaScript</div>
<div class="skill">🗄️ SQL</div><div class="skill">📊 Power BI</div>
<div class="skill">📈 Excel</div><div class="skill">📱 Flutter</div>
<div class="skill">⚛️ MERN Stack</div><div class="skill">🛍️ Shopify</div>
<div class="skill">📦 Amazon FBA</div><div class="skill">🎯 Digital Marketing</div>
<div class="skill">🔎 Data Mining</div><div class="skill">📋 Data Analysis</div>
<div class="skill">🤝 Supplier Research</div><div class="skill">💡 Problem Solving</div>
</div>
</div>
</section>

<section class="section" id="experience">
<div class="container">
<div class="heading"><div class="eyebrow">03 / Experience</div>
<h2>Learning through <span class="gradient">real work.</span></h2>
<p>Experience across software, research and e-commerce environments.</p></div>
<div class="grid">
<div class="card"><div class="card-icon">⌘</div><h3>Software & Development</h3><p>Exploring software development, Python applications, web technologies and practical programming projects.</p></div>
<div class="card"><div class="card-icon">📊</div><h3>Data Mining Internship</h3><p>Business lead research, data collection, prospect discovery and organising information for business workflows.</p></div>
<div class="card"><div class="card-icon">🛒</div><h3>E-commerce Operations</h3><p>Amazon product research, sourcing, distributor research, supplier verification and marketplace operations.</p></div>
</div>
</div>
</section>

<section class="section" id="projects">
<div class="container">
<div class="heading"><div class="eyebrow">04 / Selected work</div>
<h2>Ideas becoming <span class="gradient">projects.</span></h2>
<p>A selection of the areas I build, explore and work towards.</p></div>
<div class="grid">
<div class="card"><div class="project-number">PROJECT 01</div><div class="card-icon">✦</div><h3>Personal Portfolio</h3><p>A responsive Flask-powered portfolio showcasing my skills, interests and professional contact details.</p><span class="project-tag">Python · Flask · CSS</span></div>
<div class="card"><div class="project-number">PROJECT 02</div><div class="card-icon">▤</div><h3>Business Data Research</h3><p>A research workflow for collecting, organising and reviewing business leads and prospect information.</p><span class="project-tag">Data · Research · Excel</span></div>
<div class="card"><div class="project-number">PROJECT 03</div><div class="card-icon">◈</div><h3>E-commerce Research</h3><p>Product opportunities, supplier discovery and marketplace research for online business operations.</p><span class="project-tag">Amazon · Shopify</span></div>
</div>
</div>
</section>

<section class="section" id="services">
<div class="container">
<div class="heading"><div class="eyebrow">05 / What I do</div>
<h2>Areas where I can <span class="gradient">help.</span></h2></div>
<div class="grid">
<div class="card"><div class="card-icon">⌘</div><h3>Web Development</h3><p>Responsive web interfaces and Python-powered applications.</p></div>
<div class="card"><div class="card-icon">📊</div><h3>Data Analysis</h3><p>Data organisation, spreadsheet analysis and reporting.</p></div>
<div class="card"><div class="card-icon">🔎</div><h3>Business Research</h3><p>Lead generation, market research and supplier discovery.</p></div>
</div>
</div>
</section>

<section class="section" id="contact">
<div class="container">
<div class="heading"><div class="eyebrow">06 / Get in touch</div>
<h2>Let's create something <span class="gradient">meaningful.</span></h2>
<p>Have a project, idea or opportunity? I'd be happy to hear from you.</p></div>
<div class="contact-box">
{% if success %}<div class="success">Your message has been saved successfully.</div>{% endif %}
<form method="POST" action="/contact">
<input class="field" name="name" placeholder="Your name" required>
<input class="field" name="email" type="email" placeholder="Your email address" required>
<input class="field" name="subject" placeholder="Subject">
<textarea class="field" name="message" placeholder="Tell me about your idea..." required></textarea>
<button class="btn primary" type="submit">Submit message ↗</button>
</form>
<div class="contact-links">
<a href="mailto:iamhamza.ahmed0008@gmail.com">✉ Email me</a>
<a href="https://github.com/hamza2006-2" target="_blank" rel="noopener">⌘ GitHub profile ↗</a>
</div>
</div>
</div>
</section>
</main>
<footer><div class="container footer-row">
<span>© 2026 Hamza Ahmed. Built with purpose.</span>
<span><a href="#home">Back to top ↑</a></span>
</div></footer>
<script>
const observer=new IntersectionObserver(entries=>{
 entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('show');observer.unobserve(e.target)}})
},{threshold:.12});
document.querySelectorAll('.heading,.card,.about-grid,.skills,.contact-box').forEach(el=>{
 el.classList.add('reveal');observer.observe(el);
});
document.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>{
 document.querySelector('.links').classList.remove('open');
}));
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, success=False)

@app.route("/profile-image")
def profile_image():
    if not IMAGE.exists():
        return "hamza.jpg not found in E drive. Put it beside app.py.", 404
    return send_from_directory(str(BASE), IMAGE.name)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return "Please fill in all required fields.", 400

    new_file = not CONTACTS.exists()
    with CONTACTS.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["Date", "Name", "Email", "Subject", "Message"])
        writer.writerow([datetime.now().isoformat(), name, email, subject, message])

    return render_template_string(HTML, success=True)

if __name__ == "__main__":
    print("Hamza Ahmed Portfolio is starting...")
    print("Open: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)



