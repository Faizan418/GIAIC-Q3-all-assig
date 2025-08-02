from agents import function_tool

@function_tool
def get_career_roadmap(field: str) -> str:
    field = field.lower()

    if field == "software_engineering":
        return "1. Learn programming languages (Python, Java, etc.)\n2. Understand data structures and algorithms\n3. Build projects to showcase skills\n4. Contribute to open source\n5. Apply for internships or entry-level positions"
    
    elif field == "data_science":
        return "1. Learn statistics and probability\n2. Master data manipulation and analysis tools (Pandas, NumPy)\n3. Gain proficiency in machine learning algorithms\n4. Work on real-world datasets\n5. Build a portfolio of data science projects"

    elif field == "cybersecurity":
        return "1. Understand networking fundamentals\n2. Learn about operating systems and security protocols\n3. Get familiar with penetration testing tools\n4. Obtain relevant certifications (e.g., CompTIA Security+)\n5. Gain practical experience through labs or internships"
    
    elif field == "cloud_computing":
        return "1. Learn about cloud service models (IaaS, PaaS, SaaS)\n2. Get hands-on experience with cloud platforms (AWS, Azure, GCP)\n3. Understand cloud architecture and deployment strategies\n4. Obtain cloud certifications (e.g., AWS Certified Solutions Architect)\n5. Work on cloud-based projects"

    elif field == "artificial_intelligence":
        return "1. Study machine learning fundamentals\n2. Learn about neural networks and deep learning\n3. Gain experience with AI frameworks (TensorFlow, PyTorch)\n4. Work on AI projects and datasets\n5. Stay updated with the latest research in AI"

    elif field == "web_development":
        return "1. Learn HTML, CSS, and JavaScript\n2. Understand front-end frameworks (React, Angular)\n3. Get familiar with back-end technologies (Node.js, Django)\n4. Build full-stack applications\n5. Deploy projects on web hosting platforms"

    elif field == "mobile_development":
        return "1. Learn mobile programming languages (Swift for iOS, Kotlin for Android)\n2. Understand mobile app architecture\n3. Build and publish mobile applications\n4. Gain experience with cross-platform frameworks (Flutter, React Native)\n5. Stay updated with mobile development trends"

    elif field == "game_development":
        return "1. Learn game design principles\n2. Get familiar with game engines (Unity, Unreal Engine)\n3. Understand graphics programming and physics simulation\n4. Build and publish games\n5. Participate in game jams to improve skills"

    elif field == "devops":
        return "1. Understand software development lifecycle\n2. Learn about continuous integration and continuous deployment (CI/CD)\n3. Get hands-on experience with containerization (Docker, Kubernetes)\n4. Understand infrastructure as code (Terraform, Ansible)\n5. Work on automating deployment processes"

    elif field == "blockchain":
        return "1. Learn about blockchain technology and its applications\n2. Understand smart contracts and decentralized applications (dApps)\n3. Get familiar with blockchain platforms (Ethereum, Hyperledger)\n4. Build and deploy blockchain projects\n5. Stay updated with the latest trends in blockchain development"

    elif field == "ui_ux_design":
        return "1. Understand design principles and user experience\n2. Learn design tools (Figma, Adobe XD)\n3. Create wireframes and prototypes\n4. Conduct user research and usability testing\n5. Build a portfolio showcasing design projects"

    elif field == "digital_marketing":
        return "1. Learn about SEO, SEM, and content marketing\n2. Understand social media marketing strategies\n3. Get familiar with analytics tools (Google Analytics)\n4. Create and manage digital marketing campaigns\n5. Stay updated with the latest trends in digital marketing"

    elif field == "project_management":
        return "1. Understand project management methodologies (Agile, Scrum)\n2. Learn about project planning and scheduling\n3. Get familiar with project management tools (Jira, Trello)\n4. Develop leadership and communication skills\n5. Gain experience through managing small projects or internships"

    elif field == "networking":
        return "1. Learn networking fundamentals (TCP/IP, OSI model)\n2. Understand network protocols and configurations\n3. Get hands-on experience with networking devices (routers, switches)\n4. Obtain networking certifications (e.g., Cisco CCNA)\n5. Work on network design and troubleshooting projects"

    elif field == "it_support":
        return "1. Understand computer hardware and software basics\n2. Learn about operating systems (Windows, Linux)\n3. Get familiar with troubleshooting techniques\n4. Obtain relevant certifications (e.g., CompTIA A+)\n5. Gain practical experience through internships or help desk roles"

    elif field == "business_analysis":
        return "1. Learn business analysis fundamentals\n2. Understand requirements gathering techniques\n3. Get familiar with business process modeling\n4. Develop analytical and problem-solving skills\n5. Gain experience through internships or projects in business analysis"

    elif field == "finance":
        return "1. Understand financial principles and accounting basics\n2. Learn about financial markets and investment strategies\n3. Get familiar with financial analysis tools (Excel, financial modeling)\n4. Obtain relevant certifications (e.g., CFA, CPA)\n5. Gain practical experience through internships in finance or investment firms"

    elif field == "human_resources":
        return "1. Understand HR fundamentals and employment laws\n2. Learn about recruitment and talent management\n3. Get familiar with performance management systems\n4. Develop communication and interpersonal skills\n5. Gain experience through internships or entry-level HR roles"

    elif field == "sales":
        return "1. Understand sales fundamentals and techniques\n2. Learn about customer relationship management (CRM) systems\n3. Develop negotiation and persuasion skills\n4. Gain experience through internships or entry-level sales positions\n5. Stay updated with sales trends and strategies"

    elif field == "legal":
        return "1. Understand legal principles and frameworks\n2. Learn about contract law and compliance\n3. Get familiar with legal research and writing\n4. Develop analytical and critical thinking skills\n5. Gain experience through internships in law firms or legal departments"

    elif field == "healthcare":
        return "1. Understand healthcare systems and policies\n2. Learn about medical terminology and patient care\n3. Get familiar with healthcare regulations and compliance\n4. Develop communication and empathy skills\n5. Gain practical experience through internships or volunteer work in healthcare settings"

    elif field == "education":
        return "1. Understand educational theories and practices\n2. Learn about curriculum development and instructional design\n3. Get familiar with assessment and evaluation methods\n4. Develop communication and teaching skills\n5. Gain experience through internships or teaching assistant roles in educational institutions"

    elif field == "research":
        return "1. Understand research methodologies and ethics\n2. Learn about data collection and analysis techniques\n3. Get familiar with academic writing and publishing\n4. Develop critical thinking and problem-solving skills\n5. Gain experience through internships or research assistant positions in academic or research institutions"

    elif field == "consulting":
        return "1. Understand consulting fundamentals and methodologies\n2. Learn about problem-solving techniques\n3. Get familiar with data analysis and presentation skills\n4. Develop communication and interpersonal skills\n5. Gain experience through internships or entry-level consulting roles"

    elif field == "entrepreneurship":
        return "1. Understand business fundamentals and startup principles\n2. Learn about market research and business planning\n3. Get familiar with funding options and financial management\n4. Develop leadership and innovation skills\n5. Gain practical experience through starting a small business or working in a startup environment"

    elif field == "nonprofit":
        return "1. Understand nonprofit management and fundraising\n2. Learn about program development and evaluation\n3. Get familiar with grant writing and compliance\n4. Develop communication and advocacy skills\n5. Gain experience through internships or volunteer work in nonprofit organizations"

    else:
        return "Career roadmap not found for the specified field."
