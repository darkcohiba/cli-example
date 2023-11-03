# from rich import print as pprint

# pprint("[blue]Hello,[/blue] [red bold]Goodbye,[/red bold] have fun!")

# pprint(":vampire:")

from rich.console import Console
console = Console()

console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")




