"use strict";

const API_URL = document.location.origin;


async function make_request(method, url, data) {
    const response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    const result = await response.json();
    console.log(result);
    return result
}

async function make_post_request(url, data) {
    return await make_request("POST", url, data)
}


function contact_data() {
    return {
        email: null,
        loading: false,
        messageSent: null,
        saveEmailUrl: API_URL + "/crm/contact",
        saveEmail: async function () {
            this.loading = true;

            const data = {
                message: "Interesat de site prezentare + programari online",
                email: this.email,
            };

            const result = await make_post_request(this.saveEmailUrl, data);

            if (result.status == 'success') {
                this.message = null;
                this.messageSent = true;
                setTimeout(() => this.messageSent = null, 3000);
            } else {
                this.messageSent = false;
                setTimeout(() => this.messageSent = null, 3000);
            }

            this.loading = false;
        }
    }
}
