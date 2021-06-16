echo "STARTING BUILDING PPMI MATRICES"
sh ppmi_anticom.sh
echo "STARTING PROPAGATING"
sh propagate_anticom.sh
echo "CREATING CHART"
python prepare_scores.py
echo "FINISHED"