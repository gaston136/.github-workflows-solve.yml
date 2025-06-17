name: Genereer argumenten zonder Python

on:
  push:
    branches: [ main ]

jobs:
  generate:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Genereer argumenten met bash
      run: |
        echo "# Argumenten over gelijk loon in sport" > arguments.md
        echo "" >> arguments.md

        echo "## Pro argumenten" >> arguments.md
        PRO_BASIS=("Gelijke betaling bevordert gelijkheid tussen mannen en vrouwen."
                   "Vrouwen leveren dezelfde inspanning als mannen en verdienen gelijke beloning."
                   "Gelijke betaling stimuleert vrouwen om meer te sporten."
                   "Het is een kwestie van rechtvaardigheid en gelijke behandeling."
                   "Vrouwen verdienen respect voor hun prestaties, net als mannen.")

        for i in $(seq 1 500); do
          idx=$(( (i - 1) % 5 ))
          echo "- ${PRO_BASIS[$idx]} (variant $i)" >> arguments.md
        done

        echo "" >> arguments.md
        echo "## Contra argumenten" >> arguments.md
        CONTRA_BASIS=("Mannen trekken gemiddeld meer publiek en verdienen daardoor meer."
                      "De inkomsten uit mannen- en vrouwensport verschillen sterk."
                      "De fysieke verschillen leiden tot andere prestaties en waardering."
                      "Sponsoring en media-aandacht zijn vaak groter bij mannen."
                      "De marktwaarde van mannelijke sporters is hoger vanwege populariteit.")

        for i in $(seq 1 500); do
          idx=$(( (i - 1) % 5 ))
          echo "- ${CONTRA_BASIS[$idx]} (variant $i)" >> arguments.md
        done

    - name: Commit en push
      run: |
        git config user.name "github-actions[bot]"
        git config user.email "github-actions[bot]@users.noreply.github.com"
        git add arguments.md
        git commit -m "Automatisch gegenereerde argumenten zonder Python"
        git push
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      continue-on-error: true
