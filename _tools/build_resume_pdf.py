# -*- coding: utf-8 -*-
"""Regenerates assets/Vinodh_Kumar_Poomari_Resume.pdf (A4, 2 pages, two-column)
with the new AI Development & Products section. Run from repo root:
    python _tools/build_resume_pdf.py
"""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, FrameBreak, NextPageTemplate, PageBreak,
                                HRFlowable)

# ━━ Palette (template-guided: matches existing resume brand + site navy/blue) ━━
NAVY        = colors.HexColor('#16243d')
BLUE        = colors.HexColor('#2f6fb8')
CYAN_DARK   = colors.HexColor('#1d7f8f')
TEXT        = colors.HexColor('#1b1a18')
MUTED       = colors.HexColor('#5b6472')
SIDEBAR_BG  = colors.HexColor('#eef1f5')
RULE        = colors.HexColor('#c9d2de')

PAGE_W, PAGE_H = A4
M = 13*mm                     # outer margin
GUT = 7*mm                    # gutter between columns
COL_L_W = 60*mm               # left (sidebar) column width
COL_R_W = PAGE_W - 2*M - COL_L_W - GUT
TOP, BOT = 14*mm, 13*mm
FRAME_H = PAGE_H - TOP - BOT

OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'Vinodh_Kumar_Poomari_Resume.pdf')

def base(name, **kw):
    d = dict(fontName='Helvetica', fontSize=8.3, leading=11.2, textColor=TEXT)
    d.update(kw); return ParagraphStyle(name, **d)

# ---- styles ----
sName    = base('name', fontName='Helvetica-Bold', fontSize=21, leading=24, textColor=NAVY)
sTitle   = base('title', fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=BLUE, spaceBefore=2)
sH       = base('h', fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=NAVY, spaceBefore=9, spaceAfter=2)
sHside   = base('hside', fontName='Helvetica-Bold', fontSize=9.5, leading=12, textColor=NAVY, spaceBefore=9, spaceAfter=2)
sBody    = base('body', spaceAfter=3)
sBul     = base('bul', leftIndent=8, bulletIndent=1, spaceAfter=2.4)
sBulS    = base('buls', leftIndent=8, bulletIndent=1, spaceAfter=1.3, fontSize=7.9, leading=9.9)
sSide    = base('side', fontSize=8.2, leading=11, textColor=TEXT, spaceAfter=2.4)
sSideBul = base('sidebul', fontSize=8.2, leading=11, leftIndent=8, bulletIndent=1, spaceAfter=2.2)
sJob     = base('job', fontName='Helvetica-Bold', fontSize=8.8, leading=11.2, textColor=NAVY, spaceBefore=4.5, spaceAfter=2)
sApp     = base('app', fontName='Helvetica-Bold', fontSize=8.8, leading=11.5, textColor=CYAN_DARK, spaceBefore=4.5, spaceAfter=1.5)
sLink    = base('link', fontSize=7.8, leading=10.5, textColor=BLUE, spaceAfter=3.4)

def rule():
    return HRFlowable(width='100%', thickness=0.8, color=RULE, spaceBefore=0, spaceAfter=3)

def bullets(items, style=sBul, mark='\u2022'):
    return [Paragraph(t, style, bulletText=mark) for t in items]

def side_head(txt):
    return [Paragraph(txt, sHside), rule()]

# ---------------- content ----------------
objective = ("Results-oriented Project Management and PMO Leader with 16+ years of experience delivering "
             "enterprise transformation, strategic programs, and business-critical initiatives across Banking "
             "and Telecom sectors. Bringing proven expertise in Program Management, Portfolio Delivery, PMO "
             "Leadership, Financial Governance, Enterprise Tooling, and executive stakeholder engagement while "
             "enabling predictable outcomes through structured execution and technology-driven solutions — "
             "including hands-on design and delivery of AI-powered products. Seeking senior leadership "
             "opportunities in Program Management, Delivery Management, PMO, Portfolio Management, or "
             "Enterprise Transformation.")

contact = [
    '(+91) 74835 92435',
    'vinodh.poomari@gmail.com',
    'Bengaluru, Karnataka, India',
    '<link href="https://in.linkedin.com/in/vinodh-kumar-poomari-6b078543/">in/vinodh-kumar-poomari</link>',
]

competencies = [
    'Program Management', 'Portfolio Management', 'PMO Leadership', 'Enterprise Transformation',
    'Delivery Management', 'Financial Governance', 'AI Product Development', 'Change Management',
    'Resource Planning', 'Regulatory Compliance', 'Cross-Functional Leadership',
]

certs = ['Certified Scrum Master (CSM) — Scrum Alliance']

profile = [
    'Proven expertise in leading enterprise transformation programs while aligning strategic priorities with measurable business outcomes consistently.',
    'Extensive experience in driving cross-functional delivery, portfolio governance, and financial oversight across global banking engagements.',
    'Advanced knowledge in JIRA, Power BI, Clarity, SharePoint, and Tableau strengthening enterprise execution and decision-making.',
    'Designed and shipped three AI-powered product prototypes — <b>PM Control Tower</b>, <b>Jigglypuff</b> and <b>The Fix</b> — built end-to-end with AI-assisted development and deployed live.',
    'Demonstrating excellence in implementing Agile governance, regulatory initiatives, and scalable operating frameworks across business functions.',
    'Championing initiatives in mentoring delivery teams while accelerating execution through automation and technology-driven operational improvements.',
]

ai_apps = [
    ('PM Control Tower — Enterprise PPM Platform ("The Command Center")',
     'Enterprise Project, Program &amp; Portfolio Management platform where leadership never asks for status — '
     'live operational data aggregates into decision-ready views.',
     ['Executive Control Tower: RAG + GREY honesty, exception-first feed, traceable insights and one-click Leadership Pack with 17 sub-reports.',
      'Portfolio → Program → Project → WBS hierarchy, CPM schedule engine (critical path, float), EVM engine (CPI/SPI/EAC/VAC), RAID and governance rules engine.',
      'Agile sprints, Kanban/Calendar/Workload boards, Monte Carlo P80 forecasting, evidence bundles and investment governance (ROI/NPV/IRR).'],
     'https://pmct.vercel.app'),
    ('Jigglypuff — Unified Voice AI Assistant',
     'One local-first voice AI fusing natural conversation, deep research, meeting intelligence and human-gated tools.',
     ['Voice conversation with barge-in, empathic tone adaptation in 80+ languages, and deep-research answers with citation cards.',
      'Meeting intelligence: live timestamped transcription compiled into summaries; HITL approval gates for high-risk actions.',
      'Dashboard with automated daily worklog, ticketing, lead capture, scheduling and continuous-learning vocabulary — 100% local-first privacy.'],
     'https://jigglypuff-ai.vercel.app'),
    ('The Fix — Solution Discovery &amp; Architecture Engine',
     'Agentic AI engine that turns vague requirements into costed, dual-track technical architectures and PoC blueprints.',
     ['Global market analysis plus Agile/Lean vs Enterprise Scale architectures with KPIs, team costs and Probability-of-Success scoring.',
      'Five-agent LangGraph pipeline with live streaming, What-If re-scoring, Mermaid.js diagrams and 6-week PoC blueprints.',
      'Exports to PPT/DOC/CSV/PDF; ships as web SPA, Windows desktop (Tauri) and mobile (Capacitor/PWA).'],
     'https://the-fix-optinus.vercel.app'),
]

capco = [
    ('Senior Program Management Consultant | Capco Technology Pvt. Ltd. | Bengaluru, India | 2022 – Present', [
        '<b>Enterprise Delivery:</b> Leading strategic banking transformation programs across global portfolios, including HSBC WPB Asset Management Client Business initiatives.',
        '<b>Execution Strategy:</b> Creating project charters, business cases, delivery roadmaps, and governance models enabling structured program execution.',
        '<b>Hybrid Leadership:</b> Managing Project Management and PMO functions while directing cross-functional teams and collaborating with C-level executives on delivery priorities.',
        '<b>Delivery Recovery:</b> Identifying overdue milestones, removing execution bottlenecks, and restoring delivery commitments across multiple workstreams.',
        '<b>Portfolio Intelligence:</b> Developing Power BI reporting frameworks providing leadership with actionable portfolio insights and business visibility.',
        '<b>Technology Leadership:</b> Serving as organizational SME for JIRA, Confluence, Clarity, SharePoint, Tableau, and Power BI platforms.',
        '<b>Automation Enablement:</b> Designing AI-enabled and RPA solutions reducing manual effort through intelligent workflow automation.',
        '<b>Leadership Reporting:</b> Delivering executive presentations, strategic scorecards, portfolio updates, and monthly governance reviews for senior leadership.',
    ]),
    ('Senior Consultant | Ujjivan Small Finance Bank | Bengaluru, India | 2021 – 2022', [
        '<b>Banking Delivery:</b> Delivered liabilities and treasury initiatives from planning through production implementation across business functions.',
        '<b>Digital Transformation:</b> Launched Digital Account Opening and Video KYC solutions achieving zero audit errors during go-live.',
        '<b>Portfolio Execution:</b> Managed multi-million-dollar programs covering planning, vendor governance, deployment, and stabilization.',
        '<b>Regulatory Compliance:</b> Established RBI-compliant controls while managing CAB approvals and production release governance.',
        '<b>Analytics:</b> Built Power BI and Clarity dashboards enabling faster portfolio reviews and leadership decision-making; introduced Scrum governance.',
    ]),
    ('Senior Consultant | Capco | Bengaluru, India | 2019 – 2021', [
        '<b>Lifecycle Ownership:</b> Directed complete project lifecycles from requirements through deployment and post-production support.',
        '<b>Decision Support:</b> Developed business cases, strategic plans, Steering Committee presentations, and executive documentation.',
        '<b>Financial Governance:</b> Managed budgets, resource allocation, delivery schedules, and financial commitments ensuring controlled execution.',
        '<b>Standardization:</b> Standardized execution practices through governance reviews, milestone tracking, and continuous operational improvements.',
        '<b>Mentoring:</b> Mentored junior Project Managers while eliminating repetitive manual activities to accelerate execution efficiency.',
    ]),
    ('Assistant Manager | Gradmener Technology Pvt. Ltd. | Bengaluru, India | 2017 – 2019', [
        '<b>RPA Implementation:</b> Implemented Robotic Process Automation (RPA) streamlining business operations and execution efficiency.',
        '<b>Process Redesign:</b> Redesigned manual workflows into structured automated processes strengthening operational consistency.',
        '<b>Reporting Automation:</b> Developed automated pipeline and project reports improving visibility for business and leadership teams.',
        '<b>Transformation:</b> Established operational frameworks supporting sustainable transformation initiatives and continuous improvement.',
    ]),
    ('Senior Delivery Consultant | Capgemini India Pvt. Ltd. | India | 2013 – 2016', [
        '<b>Global PMO:</b> Led PMO operations across India, UK, Netherlands, and UAE supporting enterprise client programs.',
        '<b>ERP Delivery:</b> Delivered the Grolsch SAP implementation on a multi-million-euro budget with successful production deployment.',
        '<b>Quality:</b> Achieved zero-error audits through standardized project controls, governance practices, and delivery discipline.',
        '<b>Collaboration:</b> Implemented SharePoint environments and executive dashboards strengthening enterprise collaboration and reporting.',
        '<b>Distributed Teams:</b> Directed distributed teams while managing milestones, dependencies, and implementation activities.',
    ]),
    ('Team Lead | NTT DATA | India | 2009 – 2013', [
        '<b>Telecom Operations:</b> Managed tariff operations and digital front-end initiatives for T-Mobile and Orange, developing automated reporting solutions that improved operational monitoring and management decision-making.',
    ]),
]

education = [
    ('Master of Business Administration (MBA/PGDM) – Finance', 'Wigan and Leigh College (WLC) | 2008 | Score: 7.5/10'),
    ('Bachelor of Commerce (B.Com)', 'Bharathidasan University, Trichy | 2006 | Score: 63%'),
]

tech_skills = [
    ('Project Management Platforms', 'JIRA, Confluence, Clarity, MS Project, MS Visio'),
    ('Business Intelligence', 'Power BI, Tableau'),
    ('Collaboration Platforms', 'SharePoint, Microsoft Office 365'),
    ('Enterprise Applications', 'SAP'),
    ('Automation Technologies', 'Robotic Process Automation (RPA), Data Office Automation'),
    ('Project Methodologies', 'Agile, Scrum'),
    ('AI Solutions', 'GPT Workflow Automation, Prompt Engineering, AI-Driven Workflows, AI-Assisted Product Development'),
    ('Certification', 'Certified Scrum Master (CSM)'),
]

key_highlights = [
    'Designed and shipped three live AI product prototypes — PM Control Tower, Jigglypuff, and The Fix — covering PPM intelligence, voice AI, and agentic solution discovery.',
    'Delivered zero-audit-error digital banking implementations across multi-million-dollar strategic transformation initiatives.',
    'Led HSBC WPB Asset Management Client Business initiatives supporting enterprise-wide portfolio transformation.',
    'Served as organizational SME for JIRA, Power BI, Clarity, SharePoint, Tableau, and enterprise delivery platforms.',
    'Developed AI-enabled workflow solutions accelerating project documentation, RAID analysis, and operational execution.',
]

soft_skills = ['Strategic Thinking', 'Decision Making', 'Team Leadership', 'Analytical Thinking',
               'Problem Solving', 'Relationship Building', 'Executive Communication']

# ---------------- doc scaffold ----------------
def draw_sidebar_bg(canv, doc):
    canv.saveState()
    canv.setFillColor(SIDEBAR_BG)
    canv.rect(0, 0, M + COL_L_W + GUT/2, PAGE_H, stroke=0, fill=1)
    canv.setFillColor(NAVY)
    canv.rect(0, PAGE_H - 6*mm, PAGE_W, 6*mm, stroke=0, fill=1)
    canv.restoreState()

fL1 = Frame(M, BOT, COL_L_W, FRAME_H, id='p1L', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
fR1 = Frame(M + COL_L_W + GUT, BOT, COL_R_W, FRAME_H, id='p1R', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
fL2 = Frame(M, BOT, COL_L_W, FRAME_H, id='p2L', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
fR2 = Frame(M + COL_L_W + GUT, BOT, COL_R_W, FRAME_H, id='p2R', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

doc = BaseDocTemplate(OUT, pagesize=A4, title='Vinodh Kumar Poomari — Resume',
                      author='Vinodh Kumar Poomari', subject='Enterprise Program Delivery Leader — Resume',
                      creator='Vinodh Kumar Poomari')
doc.addPageTemplates([
    PageTemplate(id='P1', frames=[fL1, fR1], onPage=draw_sidebar_bg),
    PageTemplate(id='P2', frames=[fL2, fR2], onPage=draw_sidebar_bg),
])

story = []

# ---- page 1 : left ----
story += side_head('OBJECTIVE')
story.append(Paragraph(objective, sSide))
story += side_head('CONTACT')
story += [Paragraph(t, sSide) for t in contact]
story += side_head('CORE COMPETENCIES')
story += bullets(competencies, sSideBul)
story += side_head('CERTIFICATIONS')
story += bullets(certs, sSideBul)
story.append(FrameBreak())

# ---- page 1 : right ----
story.append(Paragraph('VINODH KUMAR POOMARI', sName))
story.append(Paragraph('ENTERPRISE PROGRAM DELIVERY LEADER  ·  AI PRODUCT BUILDER', sTitle))
story.append(Spacer(1, 2))
story.append(rule())

story.append(Paragraph('PROFILE SUMMARY', sH)); story.append(rule())
story += bullets(profile, sBulS)

story.append(Paragraph('AI DEVELOPMENT &amp; PRODUCTS — DESIGNED, BUILT &amp; SHIPPED LIVE', sH)); story.append(rule())
for title, blurb, feats, url in ai_apps:
    story.append(Paragraph(title, sApp))
    story.append(Paragraph(blurb, sBulS))
    story += bullets(feats, sBulS)
    story.append(Paragraph('<b>Live:</b> <link href="%s"><u>%s</u></link>' % (url, url.split('//')[1]), sLink))

# ---- page 2 ----
story.append(NextPageTemplate('P2'))
story.append(PageBreak())
story += side_head('EDUCATION')
for deg, meta in education:
    story.append(Paragraph('<b>%s</b>' % deg, sSide))
    story.append(Paragraph(meta, sSide))
story += side_head('TECHNICAL SKILLS')
for cat, val in tech_skills:
    story.append(Paragraph('<b>%s:</b> %s' % (cat, val), sSide))
story += side_head('KEY HIGHLIGHTS')
story += bullets(key_highlights, sSideBul)
story += side_head('SOFT SKILLS')
story += bullets(soft_skills, sSideBul)
story.append(FrameBreak())

story.append(Paragraph('WORK EXPERIENCE', sH)); story.append(rule())
for head, items in capco:
    story.append(Paragraph(head, sJob))
    story += bullets(items, sBulS)

doc.build(story)
print('WROTE', os.path.abspath(OUT))
