// Write `mergeConfigs(defaults, ...overrides)` that takes a default config object and any number of override objects, merges them all (later ones win), returns the result. Test with 3 overrides where some keys conflict. Use destructuring somewhere in the function.

function mergeConfigs(defaults, ...overrides) {
    const modified = Object.assign({}, defaults, ...overrides);
    const {
        theme, fontSize, language
    } = modified;

    console.log(`Theme is: ${theme}, Fontsize is: ${fontSize},and Language is: ${language}`);
    return modified;
}

const defaultsSettings = {
    theme: "Light",
    fontSize: 14,
    language: "en"
}

override1 = { theme: "dark" };
override2 = { fontSize: 16 };
override3 = { theme: "system", language: "hi" };

console.log(mergeConfigs(defaultsSettings, override1, override2, override3));