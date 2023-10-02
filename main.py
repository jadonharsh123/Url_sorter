def sort_urls_by_length(urls):
    sorted_urls = sorted(urls, key=lambda url: len(url))
    return sorted_urls

def main():
    # Get a list of URLs from the user
    num_of_urls = int(input("Enter the number of URLs: "))
    urls = []
    for i in range(num_of_urls):
        url = input(f"Enter URL #{i + 1}: ")
        urls.append(url)

    # Sort URLs by length
    sorted_urls = sort_urls_by_length(urls)

    # Display sorted URLs
    print("\nSorted URLs:")
    for url in sorted_urls:
        print(url)

if __name__ == "__main__":
    main()
