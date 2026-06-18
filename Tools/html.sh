#!/bin/bash

# Directory containing host folders
BASE_DIR="./screenshot"

# Output HTML file
OUTPUT="index.html"

# Start HTML
cat <<'EOF' > "$OUTPUT"
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My SS</title>
    <style>
        body {
            font-family: "JetBrains Mono", "Fira Code", Consolas, monospace;
            color: #f3f3f3;
            background-color: black;
        }

        table {
            border-collapse: collapse;
            width: 95%;
            margin: 0 auto;
        }

        th, td {
            border: 1px solid #444;
            text-align: center;
        }

        th {
            font-size: 25px;
            padding: 10px;
        }

        td:first-child {
            width: 60px;
        }

        td:nth-child(2) {
            font-size: 19px;
        }

        img {
            max-width: 800px;
            max-height: 700px;
        }

        .host-link {
            color: #f3f3f3;
            text-decoration: none;
        }

        .host-link:hover {
            text-decoration: underline;
        }

        input[type="checkbox"] {
            transform: scale(1.5);
            cursor: pointer;
        }

        .checked-row {
            opacity: 0.5;
        }
    </style>
</head>
<body>

<br>

<table>
<tr>
    <th>Done</th>
    <th>Host</th>
    <th>Screenshot</th>
</tr>
EOF

# Loop through each directory
for dir in "$BASE_DIR"/*/; do
    host="https://$(basename "$dir")"

    # Find first PNG file
    screenshot=$(find "$dir" -maxdepth 1 -iname "*.png" | head -n 1)

    if [[ -n "$screenshot" ]]; then
        cat <<EOF >> "$OUTPUT"
<tr>
    <td>
        <input type="checkbox" class="row-checkbox">
    </td>
    <td style="padding: 5px;">
        <a class="host-link" href="$host" target="_blank">$host</a>
    </td>
    <td style="padding: 10px;">
        <a href="$screenshot" target="_blank">
            <img src="$screenshot" alt="Screenshot of $host">
        </a>
    </td>
</tr>
EOF
    else
        cat <<EOF >> "$OUTPUT"
<tr>
    <td>
        <input type="checkbox" class="row-checkbox">
    </td>
    <td>$host</td>
    <td>No screenshot found</td>
</tr>
EOF
    fi
done

# Finish HTML + JavaScript
cat <<'EOF' >> "$OUTPUT"
</table>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.row-checkbox');

    checkboxes.forEach((checkbox, index) => {
        const row = checkbox.closest('tr');
        const key = 'screenshot-review-' + index;

        // Restore state
        const saved = localStorage.getItem(key);
        if (saved === 'true') {
            checkbox.checked = true;
            row.classList.add('checked-row');
        }

        // Save state
        checkbox.addEventListener('change', () => {
            localStorage.setItem(key, checkbox.checked);

            if (checkbox.checked) {
                row.classList.add('checked-row');
            } else {
                row.classList.remove('checked-row');
            }
        });
    });
});
</script>

</body>
</html>
EOF

echo "HTML report generated: $OUTPUT"
