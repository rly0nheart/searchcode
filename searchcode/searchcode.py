import logging
import argparse
import requests
import subprocess
from pprint import pprint


# Getting code results; given a searchcode unique code ID
def code_results(args, api_endpoint):
    response = requests.get(api_endpoint).json()
    pprint(response['code'])


# Querying the searchcode index
def code_search(args, api_endpoint):
    response = requests.get(api_endpoint).json()
    if args.raw:
        pprint(response['results'])
    else:
        for count, item in enumerate(response['results'], start=1):
            code_data = {"ID": item['id'],
                         "Repo": item['repo'],
                         "Lines": item['linescount'],
                         "Filename": item['filename'],
                         "Location": item['location'],
                         "Language(s)": item['language'],
                         "Search term": response['searchterm']}
            print(f"\n\nResult {count} of {response['total']}\n{item['name'].upper()}")
            for data_key, data_value in code_data.items():
                print(f"├─ {data_key}: {data_value}")
                
            for line, code in item['lines'].items():
                print(f"{line}: {code}")
            print(f"-" * 100)


# Getting related code results; given a searchcode unique code ID
def related_results(args, api_endpoint):
    response = requests.get(api_endpoint).json()
    if args.raw:
        pprint(response)
    else:
        for item in response:
            code_data  = {"ID": item['id'],
                          "Lines": item['linescount'], 
                          "Filename": item['filename'],
                          "Source": item['source'],
                          "Source URI": item['sourceurl'],
                          "Location": item['location'],
                          "Language(s)": item['language'],
                          "MD5": item['md5hash']}
            print(f"\n{item['reponame'].upper()}")
            for code_key, code_value in code_data.items():
                print(f"├─ {code_key}: {code_value}")


def check_updates():
    current_version_tag = "1.1.0"
    """
    Checks if the release tag matches the current tag in the program
    If there's a match, ignore
    """
    response = requests.get("https://api.github.com/repos/rly0nheart/searchcode-cli/releases/latest").json()
    if response['tag_name'] == current_version_tag:
        pass
    else:
        print(f"[UPDATE] A new release of searchcode-cli is available ({response['tag_name']}). Run 'pip3 install --upgrade searchcode-cli' to install the updates.")
            
            
def usage():
    return """
    Basic usage:
        # code_search 
        searchcode code_search --query <query>

        # code_result
        searchcode code_result --code-id <code_id>

        # related_results
        searchcode related_results --code-id <code_id>
        
    Docker container usage:
        # code_search 
        docker run -it rly0nheart/searchcode-cli code_search --query <query>
        
        # code_search 
        docker run -it rly0nheart/searchcode-cli relate_results --code-id <code_id>
        """


def create_parser():
    parser = argparse.ArgumentParser(description=f"searchcode-cli: official command line client for searchcode.com", epilog="Search 75 billion lines of code from 40 million projects. Helping you find real world examples of functions, API's and libraries in 243 languages across 10+ public code sources", usage=usage())
    parser.add_argument("mode", 
                        help="""options:
                                      code_search - Queries the code index and returns at most 100 results.
                                      code_result - Returns the raw data from a code file given the code id which can be found as the id in a code search result.
                                      related_result - Returns an array of results given a searchcode unique code id which are considered to be duplicates.""", 
                        choices=['code_search', 'code_result', 'related_results'])
    parser.add_argument("-q", "--query", help="search query")
    parser.add_argument("-ci", "--code-id", help="code id (can be found as ID/id in a code_search result).", dest="code_id")
    parser.add_argument("-p", "--page", help="page number (default: %(default)s)", default=1)
    parser.add_argument("-r", "--raw", help="return results in raw json format", action="store_true")
    parser.add_argument("-sf", "--source-filter", help=argparse.SUPPRESS)  # Filters feature coming soon..
    parser.add_argument("--output",help=argparse.SUPPRESS)  # Output feature coming soon..
    parser.add_argument("-d", "--debug", help="enable debug mode (shows network logs)", action="store_true")
    return parser


def searchcode():
    api_endpoint = "https://searchcode.com/api"
    arg_parser = create_parser()
    args = arg_parser.parse_args()
    check_updates()
    if args.debug:
        logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.DEBUG)
    try:
        if args.mode == "code_search":
            code_search(args, api_endpoint=f"{api_endpoint}/codesearch_I/?q={args.query}&p={args.page}&per_page=100")
        elif args.mode == "code_result":
            code_results(args, api_endpoint=f"{api_endpoint}/result/{args.code_id}")
        elif args.mode == "related_results":
            related_results(args, api_endpoint=f"{api_endpoint}/related_results/{args.code_id}")
    except KeyboardInterrupt:
        print("[CTRLC] Process interrupted with Ctrl+C.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
