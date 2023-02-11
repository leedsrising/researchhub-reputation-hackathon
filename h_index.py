import requests
import json 

OPEN_ALEX_API = "https://api.openalex.org/authors/"

def get_list_of_works(author_id: str): 
  response = requests.get(url=OPEN_ALEX_API+ f"{author_id}") 
  body = json.loads(response.content)
  works_api_url = body['works_api_url']
  works_response = requests.get(url=works_api_url) 
  return json.loads(works_response.content)

def get_h_index(author_id: str) -> int:
  works = get_list_of_works(author_id)
  citation_nums = []
  for work in works['results']:
    citation_nums.append(work['cited_by_count'])

  citation_nums.sort(reverse=True)
  h_index = 0 
  for i in range(len(citation_nums)):
    if citation_nums[i] > i+1: 
      h_index += 1
  return h_index

print(get_h_index("A2208157607"))
# Returns 16





