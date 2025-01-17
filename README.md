# BIM-based Schedule Generation and Optimization Using Genetic Algorithms

This repository contains the Python code accompanying the research paper:

**Title:** [BIM-based schedule generation and optimization using genetic algorithms](https://www.sciencedirect.com/science/article/abs/pii/S0926580524002127?via%3Dihub)

### Abstract
This research presents a transformative framework to tackle challenges within the construction industry, where efficiency is hindered by limited digitalization and disjointed project phases. The framework seamlessly integrates state-of-the-art technologies, such as Building Information Modeling (BIM), Genetic Algorithms (GAs) for schedule optimization, 5D simulation, and a Business Intelligence (BI) Dashboard. By doing so, it effectively enhances productivity while bridging the gap between the realms of management and engineering. A comprehensive literature review underpins the framework's design, focusing mainly on BIM-based schedule generation and optimization. The approach's validity is demonstrated through a compelling case study, showcasing automated BIM model creation, BIM-Based schedule generation limited to structural elements of bottom-up Cast-in-situ construction method, GAs-driven schedule optimization, 5D project simulation, and the integration of the BI dashboard. This research propels operational efficiency and promotes harmonious integration with pre-existing software systems, thus facilitating smoother adoption and adaptation.

---

## Repository Overview
This repository provides the Python implementation used for:

1. **Integration with Primavera P6 SQLite Database**:
   - Creating activities, resources, and relations in the Primavera P6 schedule database.
2. **Schedule Generation**:
   - Automating BIM-based schedule creation, focusing on structural elements of the bottom-up cast-in-situ construction method.
3. **Schedule Optimization**:
   - Implementing Genetic Algorithms (GAs) for optimizing project schedules.
4. **5D Simulation and BI Dashboard Integration**:
   - Simulating 5D project data and integrating it into a business intelligence dashboard for enhanced visualization and decision-making.

---

## Getting Started

### Prerequisites
- **Python** (>= 3.8)
- Required Python libraries (see `requirements.txt`)
- Access to Primavera P6 SQLite database

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Mohamed-Elnahla/P6-Automation
   cd P6-Automation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Database Configuration**:
   - Ensure you have access to the Primavera P6 SQLite database.
   - Update the database connection details in `config.py`.

2. **Running the Code**:
   - To create activities, resources, and relations:
     ```bash
     python create_schedule.py
     ```
   - For schedule optimization using Genetic Algorithms:
     ```bash
     python optimize_schedule.py
     ```

3. **Output**:
   - The scripts generate outputs directly in the Primavera P6 database and produce logs for review.

---

## Repository Structure
```
P6-Automation/
|
├── create_schedule.py       # Script for creating BIM-based schedules
├── optimize_schedule.py     # Script for GA-based schedule optimization
├── config.py                # Database and configuration settings
├── requirements.txt         # Python dependencies
├── README.md                # Repository documentation
└── utils/                   # Helper functions and modules
```

---

## Case Study
The code was validated through a case study described in the research paper. It demonstrates:
- Automated BIM model creation and schedule generation.
- Optimization of the schedule for structural elements of cast-in-situ construction using GAs.
- Integration with 5D simulation and BI dashboards for enhanced project insights.

---

## Authors
- Hossam Wefki
- Mohamed Elnahla
- Emad Elbeltagi

---

## Citation
If you use this code or find it helpful, please cite the research paper:

```
@article{WEFKI2024105476,
title = {BIM-based schedule generation and optimization using genetic algorithms},
journal = {Automation in Construction},
volume = {164},
pages = {105476},
year = {2024},
issn = {0926-5805},
doi = {https://doi.org/10.1016/j.autcon.2024.105476},
url = {https://www.sciencedirect.com/science/article/pii/S0926580524002127},
author = {Hossam Wefki and Mohamed Elnahla and Emad Elbeltagi},
keywords = {Building information modeling (BIM), Automation, Genetic algorithm, Automatic Scheduling, Construction, Optimization, Integrated project delivery (IPD), 5D simulation},
abstract = {This research presents a transformative framework to tackle challenges within the construction industry, where efficiency is hindered by limited digitalization and disjointed project phases. The framework seamlessly integrates state-of-the-art technologies, such as Building Information Modeling (BIM), Genetic Algorithms (GAs) for schedule optimization, 5D simulation, and a Business Intelligence (BI) Dashboard. By doing so, it effectively enhances productivity while bridging the gap between the realms of management and engineering. A comprehensive literature review underpins the framework's design, focusing mainly on BIM-based schedule generation and optimization. The approach's validity is demonstrated through a compelling case study, showcasing automated BIM model creation, BIM-Based schedule generation limited to structural elements of bottom-up Cast-in-situ construction method, GAs-driven schedule optimization, 5D project simulation, and the integration of the BI dashboard. This research propels operational efficiency and promotes harmonious integration with pre-existing software systems, thus facilitating smoother adoption and adaptation.}
}
```

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

