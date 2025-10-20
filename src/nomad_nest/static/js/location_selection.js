// app/static/js/location_selection.js

document.addEventListener("DOMContentLoaded", function () {
    const countrySelect = document.getElementById("country");
    const stateSelect = document.getElementById("state");
    const citySelect = document.getElementById("city");
    const compareBtn = document.getElementById("compare-btn");

    // Load countries
    fetch("/api/countries")
        .then(response => response.json())
        .then(data => {
            data.forEach(country => {
                let option = new Option(country.name, country.id);
                countrySelect.add(option);
            });
        });

    // Load states when country is selected
    countrySelect.addEventListener("change", function () {
        stateSelect.innerHTML = '<option value="">-- Select State --</option>';
        citySelect.innerHTML = '<option value="">-- Select City --</option>';
        stateSelect.disabled = true;
        citySelect.disabled = true;
        compareBtn.disabled = true;

        if (this.value) {
            fetch(`/api/states?country_id=${this.value}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(state => {
                        let option = new Option(state.name, state.id);
                        stateSelect.add(option);
                    });
                    stateSelect.disabled = false;
                });
        }
    });

    // Load cities when state is selected
    stateSelect.addEventListener("change", function () {
        citySelect.innerHTML = '<option value="">-- Select City --</option>';
        citySelect.disabled = true;
        compareBtn.disabled = true;

        if (this.value) {
            fetch(`/api/cities?state_id=${this.value}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(city => {
                        let option = new Option(city.name, city.id);
                        citySelect.add(option);
                    });
                    citySelect.disabled = false;
                });
        }
    });

    // Enable compare button when city is selected
    citySelect.addEventListener("change", function () {
        compareBtn.disabled = !this.value;
    });
});
