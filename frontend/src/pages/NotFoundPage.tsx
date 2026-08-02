import { Button, Paper, Typography } from "@mui/material";
import { Link } from "react-router-dom";

const NotFoundPage = () => {
  return (
    <Paper
      sx={{
        p: 5,
        m: 5,
        textAlign: "center",
      }}
    >
      <Typography variant="h2">
        404
      </Typography>

      <Typography
        sx={{
          my: 3,
        }}
      >
        Page not found.
      </Typography>

      <Button
        variant="contained"
        component={Link}
        to="/"
      >
        Back to Dashboard
      </Button>
    </Paper>
  );
};

export default NotFoundPage;