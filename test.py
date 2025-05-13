from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Union
import logging
import json
from enum import Enum, auto
import matplotlib.pyplot as plt
import pandas as pd

class JobCategory(Enum):
    """
    Darba kategoriju definīcija.
    """
    IT = auto()
    FINANCE = auto()
    MARKETING = auto()
    ENGINEERING = auto()
    SALES = auto()
    HEALTHCARE = auto()
    EDUCATION = auto()
    OTHER = auto()

@dataclass
class JobDetails:
    """
    Detalizēta darba sludinājuma klase.
    """
    title: str
    company: str
    salary: float
    location: str
    category: JobCategory
    experience_level: str
    employment_type: str
    publication_date: str
    skills: List[str]
    description: str

class JobDataPresenter:
    """
    Darba sludinājumu datu prezentācijas un analīzes klase.
    """
    def __init__(self, jobs: List[JobDetails]):
        """
        Inicializē datu prezentētāju ar darba sludinājumiem.
        
        :param jobs: Saraksts ar darba sludinājumiem
        """
        self.jobs = jobs
        self.df = pd.DataFrame([asdict(job) for job in jobs])

    def generate_salary_insights(self) -> Dict[str, Union[float, str]]:
        """
        Ģenerē detalizētu algu analīzi.
        
        :return: Algu statistikas vārdnīca
        """
        return {
            'vidējā_alga': self.df['salary'].mean(),
            'minimālā_alga': self.df['salary'].min(),
            'maksimālā_alga': self.df['salary'].max(),
            'mediāna': self.df['salary'].median(),
            'standarta_novirze': self.df['salary'].std()
        }

    def categorize_jobs(self) -> Dict[JobCategory, int]:
        """
        Kategorizē darba sludinājumus.
        
        :return: Darba sludinājumu skaits katrā kategorijā
        """
        return dict(self.df['category'].value_counts())

    def generate_location_distribution(self) -> Dict[str, int]:
        """
        Ģenerē darba sludinājumu sadalījumu pēc atrašanās vietas.
        
        :return: Darba sludinājumu skaits katrā atrašanās vietā
        """
        return dict(self.df['location'].value_counts())

    def visualize_salary_distribution(self, save_path: str = 'salary_distribution.png'):
        """
        Izveido algu sadalījuma vizualizāciju.
        
        :param save_path: Faila saglabāšanas ceļš
        """
        plt.figure(figsize=(10, 6))
        self.df['salary'].hist(bins=20, edgecolor='black')
        plt.title('Algu Sadalījums')
        plt.xlabel('Alga')
        plt.ylabel('Skaits')
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def filter_jobs(self, 
                    min_salary: Optional[float] = None, 
                    category: Optional[JobCategory] = None, 
                    location: Optional[str] = None) -> List[JobDetails]:
        """
        Filtrē darba sludinājumus pēc noteiktiem kritērijiem.
        
        :param min_salary: Minimālā alga
        :param category: Darba kategorija
        :param location: Atrašanās vieta
        :return: Filtrēti darba sludinājumi
        """
        filtered_df = self.df.copy()
        
        if min_salary is not None:
            filtered_df = filtered_df[filtered_df['salary'] >= min_salary]
        
        if category is not None:
            filtered_df = filtered_df[filtered_df['category'] == category]
        
        if location is not None:
            filtered_df = filtered_df[filtered_df['location'] == location]
        
        return [JobDetails(**row) for row in filtered_df.to_dict('records')]

    def export_to_formats(self, formats: List[str] = ['json', 'csv'], base_path: str = './exports/'):
        """
        Eksportē datus dažādos formātos.
        
        :param formats: Eksportējamie formāti
        :param base_path: Bāzes ceļš eksportam
        """
        # Nodrošina eksporta direktorijas esamību
        import os
        os.makedirs(base_path, exist_ok=True)

        for format in formats:
            export_path = f'{base_path}jobs_export.{format}'
            
            if format == 'json':
                with open(export_path, 'w', encoding='utf-8') as f:
                    json.dump(self.df.to_dict('records'), f, ensure_ascii=False, indent=2)
            
            elif format == 'csv':
                self.df.to_csv(export_path, index=False, encoding='utf-8')
            
            logging.info(f'Eksportēts fails: {export_path}')

    def generate_comprehensive_report(self) -> Dict:
        """
        Ģenerē vispusīgu darba tirgus pārskatu.
        
        :return: Detalizēts pārskats par darba sludinājumiem
        """
        return {
            'vispārīgā_statistika': {
                'sludinājumu_skaits': len(self.jobs),
                'kategorijas': self.categorize_jobs(),
                'atrašanās_vietas': self.generate_location_distribution()
            },
            'algu_statistika': self.generate_salary_insights(),
            'top_prasmes': self._get_top_skills(),
            'darba_tipi': dict(self.df['employment_type'].value_counts())
        }

    def _get_top_skills(self, top_n: int = 10) -> List[tuple]:
        """
        Iegūst visvairāk pieprasītās prasmes.
        
        :param top_n: Top prasmes, kuras parādīt
        :return: Saraksts ar top prasmēm
        """
        # Pieņemam, ka 'skills' ir saraksts
        all_skills = [skill for skills_list in self.df['skills'] for skill in skills_list]
        skill_counts = pd.Series(all_skills).value_counts()
        return list(skill_counts.head(top_n).items())

def example_usage():
    """
    Demonstrācijas funkcija datu prezentācijas izmantošanai.
    """
    # Piemēra darba sludinājumi
    jobs = [
        JobDetails(
            title='Programmētājs',
            company='Tech Latvia',
            salary=2000,
            location='Rīga',
            category=JobCategory.IT,
            experience_level='Vidējs',
            employment_type='Pilna slodze',
            publication_date='2024-05-12',
            skills=['Python', 'Django', 'React'],
            description='Meklējam pieredzējušu programmētāju...'
        ),
        JobDetails(
            title='Data zinātnieks',
            company='Data Solutions',
            salary=2500,
            location='Rīga',
            category=JobCategory.IT,
            experience_level='Augsts',
            employment_type='Pilna slodze',
            publication_date='2024-05-10',
            skills=['Python', 'Machine Learning', 'SQL'],
            description='Meklējam data zinātnieku...'
        )
    ]

    # Izveido prezentētāju
    presenter = JobDataPresenter(jobs)

    # Ģenerē un izvada pārskatu
    report = presenter.generate_comprehensive_report()
    print(json.dumps(report, indent=2, ensure_ascii=False))

    # Vizualizē algu sadalījumu
    presenter.visualize_salary_distribution()

    # Eksportē datus
    presenter.export_to_formats()

    # Filtrē darba sludinājumus
    filtered_jobs = presenter.filter_jobs(
        min_salary=1800, 
        category=JobCategory.IT, 
        location='Rīga'
    )
    print("\nFiltrētie darba sludinājumi:")
    for job in filtered_jobs:
        print(f"{job.title} - {job.company}")

if __name__ == "__main__":
    example_usage()
