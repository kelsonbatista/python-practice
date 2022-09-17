from report_loader import ReportLoader
from report_adapter import G3000LoaderAdapter
from report_analyser import ReportAnalyzer

g3000_loader = ReportLoader()
loader = G3000LoaderAdapter(g3000_loader)
# o analyzer do nosso sistema recebe o adaptador como qualquer outro loader
analyzer = ReportAnalyzer(loader)
print(analyzer.average())  # Agora funcionará
