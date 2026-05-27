# integration-bus Makefile — convenience shortcuts for the orchestrator workspace

.PHONY: help watch watch-quiet watch-loud status recent goal clean-state

help:  ## List commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

watch:  ## Live-tail state/*.jsonl with macOS notifications on high-signal events
	uv run --script watch.py

watch-quiet:  ## Same as watch, but no desktop notifications
	uv run --script watch.py --no-notify

watch-loud:  ## Notify + also append wakeup events to orchestrator.jsonl
	uv run --script watch.py --wakeup

status:  ## Dump events from the last 30 min and exit
	uv run --script watch.py --since 30m

recent:  ## Dump last 2 h then continue tailing live
	uv run --script watch.py --since 2h --tail

goal:  ## Print the current cross-project goal
	@cat goal.md

clean-state:  ## DANGER: truncate quant/kb state logs to baseline (orchestrator log untouched)
	@echo "About to truncate state/{quant,kb}.jsonl. Ctrl+C to abort, Enter to confirm."
	@read _
	@TS=$$(date -u +%Y-%m-%dT%H:%M:%S+00:00); \
		echo "{\"ts\":\"$$TS\",\"agent\":\"quant\",\"event\":\"bus_initialized\",\"summary\":\"reset by clean-state\",\"payload\":{},\"blocks_on\":null}" > state/quant.jsonl; \
		echo "{\"ts\":\"$$TS\",\"agent\":\"kb\",\"event\":\"bus_initialized\",\"summary\":\"reset by clean-state\",\"payload\":{},\"blocks_on\":null}" > state/kb.jsonl
	@echo "Truncated. orchestrator.jsonl preserved."
