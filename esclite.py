import click
import requests

@click.command()
@click.option('-l', '--language', default="l1", help="Lengua en la que deseas buscar", show_default=True)
@click.option('-q', '--query', required=True, type=str, help="Texto a buscar")
@click.option('-i', '--index', required=True, type=str, help="Indice donde buscar")
@click.option('-c', '--count', default=1, type=int,  help="Número de resultados a mostrar")
@click.option('-v', '--verbose', is_flag=True, help="Muestra más información")
def main(language, query, index, count, verbose):
    api_url = "https://api.elotl.mx/v1/search/"
    data = {"lang": language, "query": query, "index": index + '-production'}
    headers = {'content-type': 'application/json'}
    r = requests.post(api_url, headers=headers, json=data)
    results = r.json()
    total = results["total_results"]
    click.secho("esCLIte 🌽💻", fg="bright_blue")
    print()
    if verbose:
        click.secho("{:<2}. | {:<35} | {:<35} | {:<20} | {:<10}".format('i', 'L1','L2','Documento','Archivo PDF'), fg="bright_blue")
    else:
        click.secho("{:<2}. | {:<35} | {:<35}".format('i', 'L1','L2'), fg="bright_blue")
    for i, line in enumerate(results["results"][:count], start=1):
        if verbose:
            click.secho("{:<2}. {:<35} | {:<35} | {:<20} | {:<10} |".format(i, line["l1"], line["l2"],
                                                                     line["document_name"],
                                                                     line["pdf_file"]))
        else:
            click.secho("{:2}. {:<35} | {:<35} | ".format(i, line["l1"], line["l2"]))

if __name__ == "__main__":
    main()
