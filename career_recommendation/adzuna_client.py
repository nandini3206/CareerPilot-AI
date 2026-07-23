"""
CareerPilot AI
Adzuna Job Search Client
"""

import requests

from config import (
    ADZUNA_APP_ID,
    ADZUNA_API_KEY,
    ADZUNA_COUNTRY,
)


class AdzunaClient:

    BASE_URL = "https://api.adzuna.com/v1/api/jobs"

    def __init__(self):

        self.app_id = ADZUNA_APP_ID
        self.api_key = ADZUNA_API_KEY
        self.country = ADZUNA_COUNTRY

    # ==========================================================
    # Search Jobs
    # ==========================================================

    def search_jobs(
        self,
        query,
        location="India",
        results_per_page=10,
        page=1,
    ):

        print("\nSearching Adzuna...")

        url = (
            f"{self.BASE_URL}/{self.country}/search/{page}"
        )

        params = {

            "app_id": self.app_id,

            "app_key": self.api_key,

            "results_per_page": results_per_page,

            "what": query,

            "where": location,

            "content-type": "application/json",

        }

        response = requests.get(
            url,
            params=params,
            timeout=20,
        )

        if response.status_code != 200:

            print(
                f"Adzuna Error : {response.status_code}"
            )

            return []

        data = response.json()

        jobs = []

        for item in data.get("results", []):

            jobs.append({

                "title": item.get("title", ""),

                "company": item.get(
                    "company",
                    {}
                ).get(
                    "display_name",
                    ""
                ),

                "location": item.get(
                    "location",
                    {}
                ).get(
                    "display_name",
                    ""
                ),

                "salary_min": item.get(
                    "salary_min"
                ),

                "salary_max": item.get(
                    "salary_max"
                ),

                "employment_type": item.get(
                    "contract_type",
                    ""
                ),

                "description": item.get(
                    "description",
                    ""
                ),

                "redirect_url": item.get(
                    "redirect_url",
                    ""
                ),

            })

        print(f"Live Jobs Found : {len(jobs)}")

        return jobs


# ==========================================================
# Main
# ==========================================================

def main():

    client = AdzunaClient()

    jobs = client.search_jobs(

        query="Machine Learning Engineer",

        location="India",

        results_per_page=5,

    )

    print()

    for i, job in enumerate(jobs, start=1):

        print("-" * 60)

        print(f"{i}. {job['title']}")

        print(job["company"])

        print(job["location"])

        print(job["redirect_url"])


if __name__ == "__main__":

    main()