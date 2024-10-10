class StepMultipying:
    
    @staticmethod
    def run(orchestrator, pipeline) -> None:
        result=pipeline.result
        pipeline.result = orchestrator.bots.multiplier.mult(result)
        output = StepMultipying.__format_output(pipeline,result)
        orchestrator.bots.printer.print_output(output)

    def __format_output(pipeline,result):
        return f"{pipeline.step} > {result} * 4 = {pipeline.result}"