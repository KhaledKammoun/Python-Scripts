interface Participant {
    name: string;
    rating: string;
    status: string;
}

function fetchParticipants(pageNumber: number): void {
    const url = `https://codeforces.com/contestRegistrants/2051/page/${pageNumber}`; // Replace with the correct URL and contest ID

    // Fetch the page using Fetch API
    fetch(url)
        .then((response: Response) => response.text())
        .then((html: string) => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const registrantsTable = doc.getElementsByClassName("registrants")[0] as HTMLElement;

            if (!registrantsTable) {
                console.log("No registrants table found on this page.");
                return;
            }

            const rows = registrantsTable.getElementsByTagName("tr");

            // Skip the header row and process participant rows
            const participants: Participant[] = [];
            for (let i = 1; i < rows.length; i++) {
                const cells = rows[i].getElementsByTagName("td");

                if (cells.length > 0) {
                    const name = cells[0].innerText.trim(); // Assuming the first column is the name
                    const rating = cells[1].innerText.trim(); // Assuming the second column is the rating
                    const status = cells[2].innerText.trim(); // Assuming the third column is the status

                    participants.push({ name, rating, status });

                    // Check if the name includes the substring "khaledkammoun" (case-insensitive)
                    if (rating.toLowerCase().includes("00karim00".toLowerCase())) {
                        console.log(`Found participant: ${name}`);
                        console.log(`Rating: ${rating}`);
                        console.log(`Status: ${status}`);
                        return; // Stop further processing after finding the participant
                    }
                }
            }

            // Log the participants of the current page
            console.log(`Page ${pageNumber} participants:`);
            // console.log(participants);

            // Check if there's another page to load
            const nextPageButton = doc.querySelector('li a.arrow');
            if (nextPageButton) {
                fetchParticipants(pageNumber + 1);
            } else {
                console.log("No more pages.");
            }
        })
        .catch((error: Error) => {
            console.error('Error fetching the page:', error);
        });
}

// Start fetching data from page 1
fetchParticipants(1);
